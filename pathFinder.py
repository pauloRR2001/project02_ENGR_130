map =   [[0,0,0,0],
        [0,1,99,1],
        [0,1,1,1],
        [0,0,0,0],
        [1,1,0,0],
        [2,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,0]]
	       
updateMap = map

currentGoal = 2
foundGoal = True
while foundGoal == True:
    foundGoal = False

    for row in range(0, 9):
        for col in range(0, 4):
            if updateMap[row][col] == currentGoal:
                foundGoal = True
                goal_i = row
                goal_j = col

                if goal_i > 0:
                    if updateMap[goal_i - 1][goal_j] == 0:
                        updateMap[goal_i - 1][goal_j] = currentGoal + 1

                if goal_i < 8:
                    if updateMap[goal_i + 1][goal_j] == 0:
                        updateMap[goal_i + 1][goal_j] = currentGoal + 1

                if goal_j > 0:
                    if updateMap[goal_i][goal_j - 1] == 0:
                        updateMap[goal_i][goal_j - 1] = currentGoal + 1

                if goal_j < 3:
                    if updateMap[goal_i][goal_j + 1] == 0:
                        updateMap[goal_i][goal_j + 1] = currentGoal + 1
                currentGoal += 1
