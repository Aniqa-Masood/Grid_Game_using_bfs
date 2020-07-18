from random import randrange, sample
import numpy as np
import random

def grid(maze,start_pt,end_pt):
    
    num_rows = len(maze)
    num_cols = len(maze[0])

    
    visited = {end_pt: None}
    queue = [end_pt]
    while queue:
        current = queue.pop(0)
        if current == start_pt:
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return shortest_path
        adj_points = []
        '''FINDING ADJACENT PTS'''
        current_col, current_row = current
        #UP
        if current_row > 0:
            if maze[current_row - 1][current_col] == "□":
                adj_points.append((current_col, current_row - 1))
        #RIGHT
        if current_col < (len(maze[0])-1):
            if maze[current_row][current_col + 1] == "□": 
                adj_points.append((current_col + 1, current_row))
        #DOWN
        if current_row < (len(maze) - 1):
            if maze[current_row + 1][current_col] == "□":
                adj_points.append((current_col, current_row + 1))
        #LEFT
        if current_col > 0:
            if maze[current_row][current_col - 1] == "□":
                adj_points.append((current_col - 1, current_row))

        '''LOOP THROUGH ADJACENT PTS'''
        for point in adj_points:
            if point not in visited:
                visited[point] = current
                queue.append(point)


#Creating Random Array
arr=np.random.choice(list("□■"),  size=(5,5))
arrr=arr.copy()
# Request two random integers between 0 and 4, in order to put "S" and "D" once, at random position
SP =  np.random.randint(0, high=4, size=2)
EP =  np.random.randint(0, high=4, size=2)
# Extract the row and column indices
i = SP[0]
j = SP[1]

ii=EP[0]
jj=EP[1]

# Put S at the random position
arrr[i,j] = "S"
# Put E at the random position
arrr[ii,jj] = "E"

print(arrr) 
tupleSP = (j,i)
tupleEP = (jj,ii)

print(grid(arr,tupleSP,tupleEP))