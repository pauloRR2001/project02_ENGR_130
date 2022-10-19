'''
===============================================================================
ENGR 130 Program Description 
	replace this text with your program description as a comment
Assignment Information
	Assignment:     Project 2 Team 19 Navigation
	Author:         Braden Sanchez, Paulo Ramirez, David Hudson, Joshua Hirchak
                    sanch367@purdue.edu, ramir378@purdue.edu, hudso166@purdue.edu, jhircha@purdue.edu
	Team ID:        19
	
=+=============================================================================
'''


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

carAngle = 90 #We will be starting the car north, 90 degrees on the unit circle

givenMap = [[0,1,0,2],
            [1,0,1,0],
            [0,0,1,0],
            [0,0,0,0],
            [1,1,0,0],
            [0,0,0,0],
            [0,1,0,1],
            [99,1,0,0],
            [0,0,0,0]]

def Nissan2002PathFinder(updateMap):  
    currentGoal = 2
    foundGoal = True
    occurrence = 1
    while foundGoal == True: #We will need to iterate through the map every single time the number of squares required to travel increases by 1.
        foundGoal = False
    
        for row in range(len(updateMap)):
            for col in range(len(updateMap[row])): #Iterate through the map
                if occurrence == 1: #Sometimes there are two paths that the car can take, this takes that into account
                    if updateMap[row][col] == currentGoal: #Find the shortest path by reverse drawing the path from the goal to the car
                        foundGoal = True
                        goal_i1 = row
                        goal_j1 = col
                        if goal_i1 > 0: #Check if spot above current target is open to move (Cannot do on row 0)
                            if updateMap[goal_i1 - 1][goal_j1] == 0:
                                updateMap[goal_i1 - 1][goal_j1] = currentGoal + 1
        
                        if goal_i1 < 8: #Check if spot below current target is open to move (Cannot do on row 8)
                            if updateMap[goal_i1 + 1][goal_j1] == 0:
                                updateMap[goal_i1 + 1][goal_j1] = currentGoal + 1
        
                        if goal_j1 > 0: #Check Left of goal (Must be away from left wall)
                            if updateMap[goal_i1][goal_j1 - 1] == 0:
                                updateMap[goal_i1][goal_j1 - 1] = currentGoal + 1
                                
                        if goal_j1 < 3: #Check Right of goal (Must be away from right wall)
                            if updateMap[goal_i1][goal_j1 + 1] == 0:
                                updateMap[goal_i1][goal_j1 + 1] = currentGoal + 1
                        occurrence += 1
                        continue
                    
                if occurrence == 2:
                    if updateMap[row][col] == currentGoal: #Check again if there is another goal in another area to avoid bugs
                        foundGoal = True
                        goal_i2 = row
                        goal_j2 = col
                                
                        if goal_i2 != -1 and goal_j2 != -1:
                            if goal_i2 > 0: #Check if spot above current target is open to move (Cannot do on row 0)
                                if updateMap[goal_i2 - 1][goal_j2] == 0:
                                    updateMap[goal_i2 - 1][goal_j2] = currentGoal + 1
            
                            if goal_i2 < 8: #Check if spot below current target is open to move (Cannot do on row 8)
                                if updateMap[goal_i2 + 1][goal_j2] == 0:
                                    updateMap[goal_i2 + 1][goal_j2] = currentGoal + 1
            
                            if goal_j2 > 0: #Check Left of goal (Must be away from left wall)
                                if updateMap[goal_i2][goal_j2 - 1] == 0:
                                    updateMap[goal_i2][goal_j2 - 1] = currentGoal + 1
                                    
                            if goal_j2 < 3: #Check Right of goal (Must be away from right wall)
                                if updateMap[goal_i2][goal_j2 + 1] == 0:
                                    updateMap[goal_i2][goal_j2 + 1] = currentGoal + 1
                                    
                if row == len(updateMap) - 1 and col == len(updateMap[row]) - 1: #Only try again after iterating through the entire map
                    currentGoal += 1 #Increase goal by 1 to move onwards
                    occurrence = 1 #Set the occurrence count back to 1
    print(updateMap)
    return updateMap


def driveTheCar(nextdirection, carAngle):
    
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
            Drive(50,50) #Turn right for twice as long 
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


    elif nextdirection == "S":
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

    elif nextdirection == "E":
        if carAngle == 0:
            Drive(50,-50) #Forward
            display.show(Image.ARROW_N)
            sleep(765)
            Drive(0,0)
            sleep(1000)
            carAngle = 0
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
            
    elif nextdirection == "W":
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
    return carAngle
    
def directionFinder(updateMap):
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
    
    while n < 10:

        north, south, east, west = 1000, 1000, 1000, 1000
        
            
        if i != 0:
            north = updateMap[i-1][j]
            if north == 1:
                updateMap[i-1][j] += 1000
                north += 1000

        if i != 8:
            south = updateMap[i+1][j]
            if south == 1:
                updateMap[i+1][j] += 1000
                south += 1000

        if j != 0:
            west = updateMap[i][j-1]
            if west == 1:
                updateMap[i][j-1] += 1000
                west += 1000
                
        if j != 3:   
            east = updateMap[i][j+1]
            if east == 1:
                updateMap[i][j+1] += 1000
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
            print(updateMap)
            print(north, south, west, east)
            
        elif i != 0: #For all other cases where the car is not at start
            if north == updateMap[i][j] - 1:
                i -= 1
                nextdirection = "N"
        
        elif i != 8:
            if south == updateMap[i][j] - 1:
                i += 1
                nextdirection = "S"
            
        elif (j != 0):
            if west == updateMap[i][j] - 1:
                j -= 1
                nextdirection = "W"
                
        elif j!=3:
            if east == updateMap[i][j] - 1:
                j += 1
                nextdirection = "E"

        print(nextdirection)
        listtt.append(nextdirection)
        n += 1
        print(i, j)       
        carAngle = driveTheCar(nextdirection, carAngle)      
    

        
        
    Drive(0,0)
    print(listtt)

        
def main():
    newMap = Nissan2002PathFinder(givenMap)
    directionFinder(newMap)
    
    
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
