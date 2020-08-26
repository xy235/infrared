from gpiozero import LED
import json
import time

led = LED(14)

file = open("backup.txt", "r")
lines = file.readlines()
#print lines
#print len(lines)

sequence = json.loads(lines[0])
last = 0;

#print sequence

def switchLed(x):
    if x:
       led.on()
    else:
       led.off()

for i in range(len(sequence)):
    x = sequence[i]
    time.sleep(x["time"] / 1000)
    if x["value"] != last:
        switchLed(x["value"])
    last = x["value"];
