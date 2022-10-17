'''
===============================================================================
ENGR 130 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     HW6 - Task1 Functions
	Author:         Paulo Ramirez, ramir378
	Team ID:        19 (individual for this hw) 
	

=+=============================================================================
'''
"""
------------------------------------
Name of function: intCheck
Viarialbes:
        numb #Function input, number
Purpose: Checks if the input is an integer and outputs error if it is not 
Author: ramir378
------------------------------------
"""
from microbit import *
import radio
from time import sleep_us
from machine import time_pulse_us

def forward(unit):
	#wheel circumference = 20 cm
	#one block = 17.78 cm
	countsToTravel = (17.78/20) * (360) * unit
	
	nMotorEncoder[motorB] = 0
	nMotorEncoder[motorC] = 0
	nMotorEncoderTarget[motorB] = countsToTravel
	nMotorEncoderTarget[motorC] = countsToTravel
	motor[motorB] = 50
	motor[motorC] = 50
	while(nMotorRunState[motorB] != runStateIdle && nMotorRunState[motorC] != runStateIdle):
		motor[motorB] = 0
		motor[motorC] = 0
		wait1Msec(500)

def turnLeft90(unit):
	countsToTravel = (17.78/20) * (360) * unit
	
	nMotorEncoder[motorB] = 0
	nMotorEncoder[motorC] = 0
	nMotorEncoderTarget[motorB] = countsToTravel
	nMotorEncoderTarget[motorC] = countsToTravel
	motor[motorB] = 50
	motor[motorC] = -50
	while(nMotorRunState[motorB] != runStateIdle && nMotorRunState[motorC] != runStateIdle):
		motor[motorB] = 0
		motor[motorC] = 0
		wait1Msec(500)
		
def turnRight90(unit):
	countsToTravel = (17.78/20) * (360) * unit
	
	nMotorEncoder[motorB] = 0
	nMotorEncoder[motorC] = 0
	nMotorEncoderTarget[motorB] = countsToTravel
	nMotorEncoderTarget[motorC] = countsToTravel
	motor[motorB] = -50
	motor[motorC] = 50
	while(nMotorRunState[motorB] != runStateIdle && nMotorRunState[motorC] != runStateIdle):
		motor[motorB] = 0
		motor[motorC] = 0
		wait1Msec(500)

import robotbit_library as r
# Define Ports for the bank of high current output
M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4
r.setup()


def Drive(lft,rgt):
    r.motor(M2B, lft)
    r.motor(M1A, rgt)

TIME_OUT = 100000  # Increase time out to see farther, but
# this will reduce the sample rate
ECHO = pin1      # ping sensor uses a single pin for ECHO and Trigger
TRIGGER = pin1
def distance(tp, ep):
    # tp is the trigger pin and ep is the echo pin
    ep.read_digital()  # clear echo
    tp.write_digital(1)  # Send a 10 microSec pulse
    sleep_us(10)  # wait 10 microSec
    tp.write_digital(0)  # Send pulse low
    ep.read_digital()  # clear echo signal - This is needed for a
    # pingSensor
    ts = time_pulse_us(ep, 1, TIME_OUT)  # Wait for echo or time out
    if ts > 0:
        ts = ts * 17 // 100  # if system did not timeout, then send
        # back a scaled value
    return ts  # Return timeout error as a negative number (-1)
while True:
    s = pathfinder()
    if s is not None:
        dist = distance(TRIGGER, ECHO)  # set up to read as a ping)))
        # sensor same pin
        print(dist)    # use serial terminal to get information
        sleep(500)     # set for a slow update rate
        
        if s=="N":
            Drive(-255,255)
            display.show(Image.ARROW_N)
        elif s=="S":
            Drive(255,-255)
            display.show(Image.ARROW_S)
        elif s=="E":
            Drive(-255,-255)
            display.show(Image.ARROW_E)
        elif s=="W":
            Drive(255,255)
            display.show(Image.ARROW_W)
        if dist < 100:
            Drive(0,0)
            display.show(Image.HEART)
            obstacle = 0
    else:
        Drive(0,0)
    sleep(20)
#microbit stuff
from microbit import *
import robotbit_library as r

M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4
r.setup()


rot = (17.78/20) * (360)
def Drive(lft,rgt):
    r.motor(M2B, lft)
    r.motor(M1A, rgt)
def die():
    Drive(0,0)

while True:
    Drive(-50.025,50)
    sleep(725)
    die()
    if nextdirection == "E":
        Drive(-50,-50)
        display.show(Image.ARROW_E)
        sleep(725)
    elif nextdirection == "W":
        Drive(50,50)
        display.show(Image.ARROW_W)
        sleep(725)
    elif nextdirection == "N":
        Drive(-50.025,50)
        display.show(Image.ARROW_N)
        sleep(725)
        
    sleep(1000)
    
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
