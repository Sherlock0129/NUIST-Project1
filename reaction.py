from gpiozero import LED, Button
from time import sleep
from random import uniform

# Initialize hardware
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# Prompt for player names
left_name = input("Left player name is: ")
right_name = input("Right player name is: ")

# Turn LED on for a random duration between 5 and 10 seconds
led.on()
sleep(uniform(5, 10))
led.off()

# Define function to handle button press
def pressed(button):
    if button.pin.number == 14:
        print(f"{left_name} won the game")
    else:
        print(f"{right_name} won the game")
    exit()

# Bind the pressed function to button events
right_button.when_pressed = pressed
left_button.when_pressed = pressed
