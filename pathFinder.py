import numpy as np 

map = np.array([[0,0,0,0,0],
                [0,1,'s',1,0],
                [0,1,1,1,0],
                [0,0,0,0,0],
                [1,1,0,0,0],
                ['f',1,1,1,0],
                [0,1,0,1,0],
                [0,1,0,1,0],
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

x = goal[0]
y = goal[1]

i_bound, j_bound = map.shape

face = 'up'
loop = 0
while loop < 800:
    loop += 1
    
    print([x,y])
    if map[x][y] == 'f':
        print('goooooooooooooooooooallllllllll')
        break
        
    if (face == 'up') and ((y < (j_bound - 1) and map[x][y+1] != str(1))):
        x -= 1
    if (face == 'right') and ((x < (i_bound - 1)) and map[x+1][y] != str(1)):
        y += 1
    if (face == 'down') and ((y > 0) and map[x][y-1] != str(1)):
        x += 1 
    if (face == 'left') and ((x > 0) and map[x-1][y] != str(1)):
        y -= 1
    
    
    
    if ((y < (j_bound - 1) and map[x][y+1] != str(1))) and (face == 'up'):
        print('face right')
        face = 'right'
        
    if ((x < (i_bound - 1)) and map[x+1][y] != str(1)) and (face == 'right'):
        print('face down')
        face = 'down'
        
    if ((y > 0) and map[x][y-1] != str(1)) and (face == 'down'):
        print('face left')
        face = 'left'
    
    if ((x > 0) and map[x-1][y] != str(1)) and (face == 'left'):
        print('face up')
        face = 'up'


print('goal:', goal, 'end:', end)  
print('x and y:', [x,y])
print('slot value:', map[x][y])
print('bounds:', [i_bound,j_bound])





