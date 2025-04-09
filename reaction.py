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

# Initialize scores
left_score = 0
right_score = 0

# Main game loop
while True:
    print(f"\nScores: {left_name}: {left_score}, {right_name}: {right_score}")
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

    # Reset winner and wait for the next round
    winner = None
    sleep(2)  # Short break between rounds
