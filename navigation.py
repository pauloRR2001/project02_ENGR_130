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


count = 0
M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4
r.setup()

def Drive(lft,rgt):
    r.motor(M2B, lft)
    r.motor(M1A, rgt)



updateMap = [[11,12,13,14,0],
            [10,1,99,1,0],
            [9,1,1,1,0],
            [8,7,6,7,0],
            [7,6,5,6,0],
            [6,5,4,5,0],
            [5,4,3,4,0],
            [4,3,2,3,0],
            [5,4,3,4,0],
            [0,0,0,0,0]]

    
def pathReader(updateMap):
    nextdirection = 'test'
    i = -1
    j = 0
    start_i = 0
    start_j = 0
    for row in updateMap:
        i = i + 1
        j= 0
        for column in row:
               j = j + 1
               if column == 99:
                   start_i = i
                   start_j = j - 1
    i = start_i
    j = start_j
    
    n = 0
    listtt = []
    countn = 0
    counts = 0
    countw = 0
    counte = 0
    rotation1 = 0
    rotation2 = 0
    while n < 10:

        north, south, east, west = 1000, 1000, 1000, 1000
        print(nextdirection)
        listtt.append(nextdirection)

        movement(nextdirection) #callllllllll

        n += 1
        print(i, j)
        if i!= 0:
            north = updateMap[i-1][j]
            if north == 1:
                north += 1000

        if i != 8:
            south = updateMap[i+1][j]
            if south == 1:
                south += 1000

        if j!=0:
            west = updateMap[i][j-1]
            if west == 1:
                west += 1000
                
        if j!=3:   
            east = updateMap[i][j+1]
            if east == 1:
                east += 1000

        print(north, south, west, east)
        
        if i != 0:
            if (north < south) and (north < west) and (north < east) and (north != 1):
                i -= 1
                display.show(Image.HAPPY)
                nextdirection = "N"
                
        
        if i != 8:
            if (south < north) and (south < west) and (south < east) and (south != 1):
                i += 1
                nextdirection = "S"
            
        if (j != 0):
            if (west < south) and (west < north) and (west < east) and (west != 1):
                j -= 1
                nextdirection = "W"
                
        if j!=3:
            if (east < south) and (east < west) and (east < north) and (east != 1):
                j += 1
                nextdirection = "E"
                
    #David's failed if statements    
        face = nextdirection
        if nextdirection == 'W':
            countw += 1
        elif nextdirection == 'E':
            counte += 1
        elif nextdirection == 'S':
            counts += 1

        if countw%2 != 0:
            nextdirection 
        elif counte%2 != 0:

        elif counts%2 != 0:
                nextdirection
        
    Drive(0,0)
    print(listtt)


def movement(nextdirection, rotation1, rotation2):
    if nextdirection == "N":
        Drive(50+rotation1,-50+rotation2)
        display.show(Image.ARROW_N)
        sleep(765)
        Drive(0,0)
        sleep(1000)
        
    elif nextdirection == "E":
        Drive(-50,-50)
        display.show(Image.ARROW_E)
        sleep(380)
        Drive(0,0)
        sleep(500)
        Drive(50,-50)
        display.show(Image.ARROW_N)
        sleep(765)
        Drive(0,0)
        display.show(Image.CHESSBOARD)
        sleep(1000)
        
    elif nextdirection == "W":
        Drive(50,50)
        display.show(Image.ARROW_W)
        sleep(380)
        Drive(0,0)
        sleep(500)
        Drive(50,-50)
        display.show(Image.ARROW_N)
        sleep(765)
        Drive(0,0)
        display.show(Image.CHESSBOARD)
        sleep(1000)
        
    elif nextdirection == "S":
        Drive(-50,-50)
        display.show(Image.ARROW_S)
        sleep(720)
        Drive(0,0)
        sleep(500)
        Drive(50,-50)
        display.show(Image.ARROW_N)
        sleep(765)
        Drive(0,0)
        display.show(Image.CHESSBOARD)
        sleep(1000)
        
    elif nextdirection == "STOP":
        Drive(0,0)
        display.show(Image.HAPPY)

    else:
        Drive(0,0)
        
    Drive(0,0)
        

def main():

    pathReader(updateMap)
if __name__ == "__main__":
    main()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
