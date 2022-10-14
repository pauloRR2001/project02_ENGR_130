'''
===============================================================================
ENGR 130 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Project 2 Team 19
	Author:         Braden Sanchez, David Hudson, Paulo Ramirez, Joshua Hirchak,
			sanch367@purdue.edu, hudso166@purdue.edu, ramir378@purdue.edu, jhircha@purdue.edu
	Team ID:        19
	

=+=============================================================================
'''
"""
#0 = open space
#1 = barrier
#2 = goal
#99 = robot


"""

def main():
	WavefrontSearch()
	NavigateToGoal()
	wait1Msec(5000)

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




# write your code here (and delete this comment)
# ----------------------------
# Inputs
# ----------------------------

# ----------------------------
# Computations
# ----------------------------

# ----------------------------
# Outputs
# -----------------------------


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
