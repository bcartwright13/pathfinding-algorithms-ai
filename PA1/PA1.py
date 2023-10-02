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
#print(start)
#print(goal)
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
#print(cost[0][0])
'''
Now that we have all of our starting info we need to created the basics for bfs. We do not need to create a arr for visited since 
we have the array that represents if it has been visited. We need to created our queue 
'''
def generate_successor(curr):
    print("testin1")
    row = curr[0]
    col = curr[1]
    print("testin2")
    up   = (row - 1, col)
    down = (row + 1, col)
    left = (row, col - 1)
    right= (row, col + 1)
    print("testin3")
    return up, down, left, right


def BFS(start,goal,cost,arr):
    start_time = time.time()
    path = []
    path.append(start)
    curr = queue.Queue()
    curr.put(start)
    #print(f'testing: {curr.get()[0]}')
    # now we need to check our cardinal points to make sure we are in bounds of our arr for l,r,u,d 
    # if we do expand to that side we need to check our cost array and make sure that it is not a 0 if it is a zero we need to stop there otherwise keep exanding.
    # create a path array to keep track of path maybe not sure how we can we track of the cost and the path together maybe a tuple??
    #(row,col)
    #each one of these is going to have a statement to check if that value has already been seen and then we need to compare it with the cost  
    #while timer is less than 3 minutes keep searching 
    while(True):
        print(f' this is curr {curr.get()}')
        up,down,left,right = generate_successor(curr.get())
        print(up)
        #up
        if(0 <= up[0] < len(arr) and 0 <= up[1] < len(arr[0]) and arr[up[0]][up[1]] == 0):
            print('testing up')
            curr.put(up)
        #down
        if(down[0] >= len(arr) and arr[down[0]][down[1]] == 0):
            print('testing down')
            curr.put(down)
        #left
        if(0 <= left[0] < len(arr) and 0 <= left[1] < len(arr[0]) and arr[left[0]][left[1]] == 0):
            print('testing left')
            curr.put(left)
        #right 
        if(0 <= right[0] < len(arr) and 0 <= right[1] < len(arr[0]) and arr[right[0]][right[1]] == 0):
            print('testing right')
            curr.put(right)
        #Statement to check that my time is still valid 
        elapsed_time = time.time() - start_time
        if elapsed_time >= 10:
            break  # Exit the loop if 10 seconds have passed
    while not curr.empty():
        print(curr.get())


        
BFS(start,goal,cost,arr)


'''
we need to before we exapnd on a path we need to first compare the cost of the other sides 

i.e. curr cost = 0 
    cost to go left,right,up,down = (2,4,2,1)
    we would expand on down since it has the least ammount of cost 
    WE NEED TO FIND ALL THE PATHS FROM THE SOURCE TO THE GOAL
    



'''