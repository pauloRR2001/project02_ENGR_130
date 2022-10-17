'''
===============================================================================
ENGR 130 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     e.g.  Exam 1 - Question 16
	Author:         Name, login@purdue.edu
	Team ID:        ## 
	

=+=============================================================================
'''
import numpy as np 

map = np.array([[0,0,0,0,0],
                [0,1,'s',1,0],
                [0,1,1,1,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [1,1,1,1,0],
                [0,0,0,1,0],
                [0,1,'f',1,0],
                [0,1,1,1,0],
                [0,0,0,0,0]])

i = 0
j = 0

goal = []

for row in map:
    i = i + 1
    j = 0
    for column in row:
        j = j + 1
        if column == 's':
            goal.append(i - 1)
            goal.append(j - 1)

i = 0
j = 0

end = []

for row in map:
    i = i + 1
    j = 0
    for column in row:
        j = j + 1
        if column == 'f':
            end.append(i - 1)
            end.append(j - 1)

print(goal)
print(end)
print(map[goal[0]][goal[1]])
print(map[end[0]][end[1]])

x = goal[0]
y = goal[1]

loop = 0
while loop < 100:
    loop += 1
    
    if map[x][y] == 'f':
        print('goooooooooooooooooooallllllllll')
        break
    
    if map[x-1][y] == str(0):
        print('up')
        x -= 1
        print([x,y])
        continue
        
    if map[x][y+1] == str(0):
        print('right')
        y += 1
        continue
        
    if map[x+1][y] == str(0):
        print('down')
        x += 1
        continue
        
    if map[x][y-1] == str(0):
        print('left')
        y -= 1
        continue
    

print(map[x][y])





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
