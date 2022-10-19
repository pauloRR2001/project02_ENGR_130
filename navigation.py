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
    return 0



updateMap = [[11,12,13,14],
            [10,1,99,1],
            [9,1,1,1],
            [8,7,6,7],
            [7,6,5,6],
            [6,5,4,5],
            [5,4,3,4],
            [4,3,2,3],
            [5,4,3,4]]


def driveTheCar(nextdirection):
    
    carAngle = 90
    
    if nextdirection == "N":
        if carAngle == 90:
            Drive(50,-50)
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
        elif carAngle == 0:
            Drive(-50,-50) #turn left
            display.show(Image.ARROW_E)
            sleep(380)
            Drive(50,-50)
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 90
        elif carAngle == 180:
            Drive(50,50) #turn right
            display.show(Image.ARROW_W)
            sleep(380)
            Drive(50,-50)
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 90
        elif carAngle == 270:
            Drive(50,50) #Turn left for twice as long 
            display.show(Image.ARROW_W)
            sleep(720)
            Drive(0,0)
            sleep(500)
            Drive(50,-50)
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            display.show(Image.CHESSBOARD)
            sleep(1000)
            carAngle = 90


    if nextdirection == "S":
        if carAngle == 270:
            Drive(50,-50)
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
        elif carAngle == 180:
            Drive(-50,-50) #turn left
            display.show(Image.ARROW_E)
            sleep(380)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 270
        elif carAngle == 0:
            Drive(50,50) #turn right
            display.show(Image.ARROW_W)
            sleep(380)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 270
        elif carAngle == 90:
            Drive(50,50) #Turn right twice as long 
            display.show(Image.ARROW_W)
            sleep(720)
            Drive(0,0)
            sleep(500)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            display.show(Image.CHESSBOARD)
            sleep(1000)
            carAngle = 270

    if nextdirection == "E":
        if carAngle == 0:
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
        elif carAngle == 270:
            Drive(-50,-50) #turn left
            display.show(Image.ARROW_E)
            sleep(380)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 0
        elif carAngle == 90:
            Drive(50,50) #turn right
            display.show(Image.ARROW_W)
            sleep(380)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 0
        elif carAngle == 180:
            Drive(50,50) #Turn right twice as long 
            display.show(Image.ARROW_W)
            sleep(720)
            Drive(0,0)
            sleep(500)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            display.show(Image.CHESSBOARD)
            sleep(1000)
            carAngle = 0
            
    if nextdirection == "W":
        if carAngle == 180:
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
        elif carAngle == 90:
            Drive(-50,-50) ##turn left
            display.show(Image.ARROW_E)
            sleep(380)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 180
        elif carAngle == 270:
            Drive(50,50) #turn right
            display.show(Image.ARROW_W)
            sleep(380)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 180
        elif carAngle == 0:
            Drive(50,50) #Turn right twice as long 
            display.show(Image.ARROW_W)
            sleep(720)
            Drive(0,0)
            sleep(500)
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            display.show(Image.CHESSBOARD)
            sleep(1000)
            carAngle = 180
    else:
        Drive(0,0)
        
    Drive(0,0)
    
def pathReader(updateMap):
    nextdirection = ""
    start_i = 0
    start_j = 0
    for row in range(len(updateMap)):
        for col in range(len(updateMap[row])):
            if updateMap[row][col] == 99:
                start_i = row
                start_j = col
                
    i = start_i
    print(i)
    j = start_j
    print(j)
    
    n = 0
    listtt = []
    
    while n < 15:

        north, south, east, west = 1000, 1000, 1000, 1000
        
            
        if i != 0:
            north = updateMap[i-1][j]
            if north == 1:
                north += 1000

        if i != 8:
            south = updateMap[i+1][j]
            if south == 1:
                south += 1000

        if j != 0:
            west = updateMap[i][j-1]
            if west == 1:
                west += 1000
                
        if j != 3:   
            east = updateMap[i][j+1]
            if east == 1:
                east += 1000

        if i == start_i and j == start_j: #To make the first move when start is 99
            if i != 0:
                if north < south and north < west and north < east:
                    i -= 1
                    nextdirection = "N"
            if i != 8:
                if south < north and south < west and south < east:
                    i += 1
                    nextdirection = "S"
            if j != 3:
                if east < south and east < west and east < north:
                    j += 1
                    nextdirection = "E"
            if j != 0:
                if west < south and west < north and west < east:
                    j -= 1
                    nextdirection = "W"
            
            print(north, south, west, east)
            
        if i != 0:
            if north == updateMap[i][j] - 1:
                i -= 1
                nextdirection = "N"
        
        if i != 8:
            if south == updateMap[i][j] - 1:
                i += 1
                nextdirection = "S"
            
        if (j != 0):
            if west == updateMap[i][j] - 1:
                j -= 1
                nextdirection = "W"
                
        if j!=3:
            if east == updateMap[i][j] - 1:
                j += 1
                nextdirection = "E"

        print(nextdirection)
        listtt.append(nextdirection)
        n += 1
        print(i, j)       
        driveTheCar(nextdirection)      
    

        
        
    Drive(0,0)
    print(listtt)



        

def main():
    #pathReader(updateMap)
    Drive(50, 50)
    sleep(380)
    Drive(0,0)
    
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
