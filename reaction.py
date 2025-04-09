from gpiozero import LED, Button
from time import sleep
from random import uniform

# Initialize hardware
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# Turn LED on for a random duration between 5 and 10 seconds
led.on()
sleep(uniform(5, 10))
led.off()

# Define function to handle button press
def pressed(button):
    if button.pin.number == 14:
        print("Left button won the game")
    else:
        print("Right button won the game")
    exit()

# Bind the pressed function to button events
right_button.when_pressed = pressed
left_button.when_pressed = pressed
