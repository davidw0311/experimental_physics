#!/usr/bin/env python

import os
import subprocess
import json
import time
import click
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PINroomvalve = 19
PINvacuumvalve = 26
GPIO.setup(PINvacuumvalve, GPIO.OUT)
GPIO.setup(PINroomvalve, GPIO.OUT)

def controlVacuum(vacuumvalve=None, roomvalve=None):
    """Use to open the two control valves for a fixed period of time. You may
    close the valve prematurely by interrupting the program using Ctrl-C.
    You can enquire about pump and valve status with option --status. Refrain
    from starting and stopping the pump. Start at the beginning and shutoff
    at the end of our experiment. Valid boolean for off=0 and on=1"""

    if vacuumvalve is not None:
        click.echo("Opening Vac Valve, pump is sucking on chamber (provided it's on)...")
        GPIO.output(PINvacuumvalve, GPIO.HIGH)
        try:
            vacuumvalve = min(vacuumvalve, 600)
            click.echo('waiting {0} seconds'.format(vacuumvalve))
            time.sleep(vacuumvalve)
        except KeyboardInterrupt:
            print('Keyboard Interrupt Detected')
        GPIO.output(PINvacuumvalve, GPIO.LOW)
        click.echo('Closing Vac Valve, chamber isolated from vacuum pump')
    if roomvalve is not None:
        click.echo('Opening Room Valve, air is coming into chamber ...')
        GPIO.output(PINroomvalve, GPIO.HIGH)
        try:
            roomvalve = min(roomvalve, 600)
            click.echo('waiting {0} seconds'.format(roomvalve))
            time.sleep(roomvalve)        
        except KeyboardInterrupt:
            print('Keyboard Interrupt Detected')
        click.echo('Closing Vac Valve, chamber isolated from room air')
        GPIO.output(PINroomvalve, GPIO.LOW)

if __name__ == '__main__':
    switch()
