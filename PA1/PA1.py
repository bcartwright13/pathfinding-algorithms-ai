import numpy as np 
import queue
#Breadth First Search 
'''
We first need to read the file so we could get the starting dimensions, starting location, and our end goal for our search algorithm
'''


f = open("/Users/johnatan/Desktop/Fall2023/AI/PA1/Test1.txt","r")
dims = f.readline().split()
start = f.readline().split()
goal = f.readline().split()
f.close()
arr = np.zeros((int(dims[0]), int(dims[1])),dtype=np.int8)
start = (int(start[0]),int(start[1]))
goal = (int(goal[0]),int(goal[1]))
arr[int(start[0]),int(start[1])] = 1
arr[int(goal[0]),int(goal[1])] = -1
print(start)
print(goal)
print(arr)

with open('/Users/johnatan/Desktop/Fall2023/AI/PA1/Test1.txt', 'r') as file:
    # Read the file line by line
    lines = file.readlines()

# Skip the first 3 lines
lines_to_skip = 3
remaining_lines = lines[lines_to_skip:]

cost = []
for line in remaining_lines:
    numbers = line.strip().split()
    cost.append(numbers)
print(cost)
'''
Now that we have all of our starting info we need to created the basics for bfs. We do not need to create a arr for visited since 
we have the array that represents if it has been visited. We need to created our queue 
'''

def BFS(start,end,cost):
    curr = queue.Queue()
    curr.put(start)
    #if():
    return 0
