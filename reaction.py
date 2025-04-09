from gpiozero import LED, Button
from time import sleep, time
from random import uniform

# Initialize hardware
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# Prompt for player names
left_name = input("Left player name is: ")
right_name = input("Right player name is: ")

# Ask for number of rounds
total_rounds = int(input("Enter number of rounds to play: "))

# Initialize scores
left_score = 0
right_score = 0

# Round counter
current_round = 1

# Main game loop
while current_round <= total_rounds:
    print(f"\nRound {current_round}/{total_rounds}")
    print(f"Scores: {left_name}: {left_score}, {right_name}: {right_score}")
    print("Get ready...")
    sleep(2)  # Preparation time

    # Turn LED on for a random duration
    led.on()
    on_time = uniform(5, 10)
    sleep(on_time)
    led.off()

    # Record the time when LED turns off
    start_time = time()
    winner = None
    reaction_time = 0

    # Define function to handle button press
    def pressed(button):
        global winner, reaction_time, left_score, right_score
        if winner is None:  # Ensure only the first press is recorded
            reaction_time = time() - start_time
            if button.pin.number == 14:
                winner = left_name
                print(f"{left_name} won this round! Reaction time: {reaction_time:.2f} seconds")
                left_score += 1
            else:
                winner = right_name
                print(f"{right_name} won this round! Reaction time: {reaction_time:.2f} seconds")
                right_score += 1

    # Bind the pressed function to button events
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed

    # Wait for player reaction (up to 5 seconds)
    sleep(5)
    if winner is None:
        print("No one pressed in time!")

    # Reset winner and prepare for the next round
    winner = None
    current_round += 1
    sleep(2)  # Short break between rounds

# Print final scores after all rounds
print("\nGame Over!")
print(f"Final Scores:\n{left_name}: {left_score}\n{right_name}: {right_score}")
if left_score > right_score:
    print(f"{left_name} wins the game!")
elif right_score > left_score:
    print(f"{right_name} wins the game!")
else:
    print("It's a tie!")
