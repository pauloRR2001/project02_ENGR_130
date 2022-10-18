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
import robotbit_library as r

import pathFinder as path


count = 0
M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4
r.setup()

def Drive(lft,rgt):
    r.motor(M2B, lft)
    r.motor(M1A, rgt)


nextdirection = pathfinder()

def movement(nextdirection):
    
    while True:
        if nextdirection == "N":
            Drive(-50,50)
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            continue
        elif nextdirection == "E":
            Drive(-50,-50)
            display.show(Image.ARROW_E)
            sleep(365)
        elif nextdirection == "W":
            Drive(50,50)
            display.show(Image.ARROW_W)
            sleep(365)
        elif nextdirection == "N":
            Drive(-50,50)
            display.show(Image.ARROW_N)
            sleep(365)
        elif nextdirection == "S":
            Drive(-50,-50)
            display.show(Image.ARROW_S)
            sleep(725)
        Drive(0,0)
        sleep(1000)
        Drive(-50,50)
        display.show(Image.CHESSBOARD)
        sleep(1000)
	
	return ([i,j])

def obstacleScanner([i,j], updateMap)
    
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
