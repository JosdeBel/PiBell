#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def switchLedCallback(channel):
    if GPIO.input(10):
        GPIO.output(17, GPIO.HIGH)
#        time.sleep(0.2)
#        GPIO.output(17, GPIO.LOW)
    else:
        GPIO.output(17, GPIO.LOW)

GPIO.add_event_detect(10, GPIO.BOTH, callback=switchLedCallback)

try:
    while True:
        time.sleep(1000)
finally:
    GPIO.cleanup()

