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



'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
