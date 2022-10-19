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
                
    return updateMap
