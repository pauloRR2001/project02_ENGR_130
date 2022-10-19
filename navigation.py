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
    j = start_j
    print('Start Point:')
    print(i, j)
    
    n = 0
    listtt = []
    
    while n < 10: #This number is modified based on how many movements are required

        north, south, east, west = 1000, 1000, 1000, 1000
        
        #North, south, east, and west are the respective values of the tiles on the map surrounding the car.
        if i != 0: #Index error bug evation
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
	#This section of conditional statements is responsible for the first movement only
	#The car can only detect tiles that are one less than the one its currently on, so this was necessary when the start is 99.
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
            
        if i != 0: #For all other cases where the car is not at start
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

        listtt.append(nextdirection)
        n += 1       
        print("\nCurrent Direction of Movement:")
        print(nextdirection)
        print("Current Location:")
        print(i, j)
        driveTheCar(nextdirection)
        
    Drive(0,0)
    print(listtt)
