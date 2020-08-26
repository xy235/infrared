from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO
import keyboard
import json
from datetime import datetime

inputPin = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin, GPIO.IN)

#def cb(channel):
#    print("hello")

raw_input("press enter when ready\n>")

class Input:
    def __init__(self, value, time):
        self.value = value
        self.time = time

started = False
sequence = []
sameCount = 0
last = 1

epoch = datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

led = LED(14)
ledOn = False
dt = datetime.now()
lastTime = unix_time_millis(dt)

#GPIO.add_event_detect(inputPin, GPIO.RISING, callback=cb)

print("Hello")

try:
    while sameCount < 100:
	isOn = GPIO.input(inputPin)
        dt = datetime.now()
        millis = unix_time_millis(dt)
	if started and isOn != last:
                sequence.append(Input(isOn, millis - lastTime))
                lastTime = millis
#	print(str(inputPin) + " is: " + str(isOn))
#        if keyboard.is_pressed('q'):
#            print("exitting")
#            break
        if isOn == 0:
	    if started == False:
	        started = True
                sequence.append(Input(isOn, millis - lastTime))
		lastTime = millis
#            print("off")
#            ledOn = False
#            led.on()
#        else:
#            print("on")
#            ledOn = True
#            led.off()
#        sleep(1)
	if started and isOn == last:
		sameCount = sameCount + 1
	else:
		sameCount = 0
	last = isOn
    with open("output.txt", "w") as outfile:
        json.dump([ob.__dict__ for ob in sequence], outfile)
        #outfile.write("\n".join(str(item) for item in sequence))
    #for x in range(len(sequence)):
        #print sequence[x]

finally:
    GPIO.cleanup()
