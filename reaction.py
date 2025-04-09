from gpiozero import LED
from time import sleep

# Initialize LED on GPIO4
led = LED(4)

# Turn LED on, wait 5 seconds, then turn off
led.on()
sleep(5)
led.off()
