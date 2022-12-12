#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
valvePIN = 19
GPIO.setup(valvePIN, GPIO.OUT)


def controlSwitch(on):
    if on:
        GPIO.output(valvePIN, GPIO.HIGH)
        print("Switch on!")
    else:
        GPIO.output(valvePIN, GPIO.LOW)
        print('Switch off!')


