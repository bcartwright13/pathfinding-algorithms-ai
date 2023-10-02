import numpy as np 
import time 
import queue
#Breadth First Search 
'''
We first need to read the file so we could get the starting dimensions, starting location, and our end goal for our search algorithm
'''


f = open("Test1.txt","r")
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

with open('Test1.txt', 'r') as file:
    # Read the file line by line
    lines = file.readlines()

# Skip the first 3 lines
lines_to_skip = 3
remaining_lines = lines[lines_to_skip:]

cost = []
for line in remaining_lines:
    numbers = line.strip().split()
    cost.append(numbers)
print(cost[0][0])
'''
Now that we have all of our starting info we need to created the basics for bfs. We do not need to create a arr for visited since 
we have the array that represents if it has been visited. We need to created our queue 
'''

def BFS(start,goal,cost,arr):
    starttime = time.time()
    curr = queue.Queue()
    curr.put(start)
    # now we need to check our cardinal points to make sure we are in bounds of our arr for l,r,u,d 
    # if we do expand to that side we need to check our cost array and make sure that it is not a 0 if it is a zero we need to stop there otherwise keep exanding.
    # create a path array to keep track of path maybe not sure how we can we track of the cost and the path together maybe a tuple??
    if(curr.get()[0] - 1 > len(arr[0])):
        print(test)
    
    #print(endtime-starttime)


'''
def generate_successor(self, state):
    row, col = state
    candidates = [
        ("Up", (row - 1, col)),
        ("Down", (row + 1, col)),
        ("Left", (row, col - 1)),
        ("Right", (row, col + 1))
    ]'''
        
BFS(start,goal,cost,arr)