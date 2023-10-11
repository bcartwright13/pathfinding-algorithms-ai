from collections import deque
import heapq
import time



class Node:
    def __init__(self, coord, cost = 0,parent=None, depth=0):
        #parent node storage
        self.parent = parent
        self.coord = coord
        #cost stores the distance to travel
        self.cost = cost
        self.depth = depth
        #heuristic distance
        self.heuristic = 0
        #heuristic + cost
        self.total_cost = 0
        

def results(end_node, nodes_expanded, max_nodes, elapsed_time):
    if end_node:
        total_cost = 0
        path = []
        while end_node:
            path.append(end_node.coord)
            total_cost += end_node.cost
            end_node = end_node.parent
        path = path[::-1]
        print("Path Found!")
        print("Total Cost:", total_cost)
        print("Number of nodes expanded:", nodes_expanded)
        print("Max nodes stored in memory:", max_nodes)
        print("Total time: {:.9f} seconds".format(elapsed_time))
        print("Path sequence:", path)
    else:
    
        print("No path found.")
        print("Number of nodes expanded:", nodes_expanded)
        print("Max nodes stored in memory:", max_nodes)
        print("Total time: {:.9f} seconds".format(elapsed_time))

def manhanttan_distance(current_node_coord, goal_node_coord):
    return abs(current_node_coord[0] - goal_node_coord[0]) + abs(current_node_coord[1] - goal_node_coord[1])

def a_star(dimensions, start, goal, map_grid):
    rows, cols = dimensions
    start_node = Node(start, 0, None, None)
    start_node.heuristic = manhanttan_distance(start,goal)
    start_node.total_cost = start_node.heuristic
    priority_queue = [(start_node.total_cost, 0, start_node)] # 0 is the counter/tie-breaker
    visited = set()
    counter = 1 # counter for tie-breaking in heap check
    nodes_expanded = 0
    max_nodes_in_memory = 1

    while priority_queue:
        _, _, current_node = heapq.heappop(priority_queue) 
        if current_node.coord in visited:
            continue
        nodes_expanded += 1
        
        visited.add(current_node.coord)
        r, c = current_node.coord
        if (r,c) == goal:
            return current_node, nodes_expanded, max_nodes_in_memory
        directions = [(r-1 ,c), (r + 1, c), (r, c + 1), (r, c - 1)]
        for dr, dc in directions:
            if 0 <= dr < rows and 0 <= dc < cols and map_grid[dr][dc] != 0 and (dr,dc) not in visited:
                total_distance = current_node.cost + map_grid[dr][dc]
                new_heuristic = manhanttan_distance((dr,dc), goal)
                new_node = Node((dr,dc), total_distance, current_node)
                new_node.heuristic = new_heuristic
                new_node.total_cost = total_distance + new_heuristic
                heapq.heappush(priority_queue, (new_node.total_cost, counter, new_node)) # use the counter as a tie-breaker
                counter += 1 # increment the counter
            current_nodes_in_memory = len(priority_queue) + len(visited)
            if current_nodes_in_memory > max_nodes_in_memory:
                max_nodes_in_memory = current_nodes_in_memory
    return None,nodes_expanded,max_nodes_in_memory



    

def bfs(dimensions, start, goal, map_grid):
    startTime = time.time()
    rows, cols = dimensions
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    nodes = {start: Node(start, map_grid[start[0]][start[1]])}
    max_nodes = len(queue)
    nodes_expanded = 0

    while queue:
        elapsed_time = time.time() - startTime
        if elapsed_time > timer:  # 180 seconds = 3 minutes
            print("3-minute time cutoff reached!")
            return None, nodes_expanded, max_nodes
        max_nodes = max(max_nodes, len(queue))
        r, c = queue.popleft()
        current_node = nodes[(r, c)]
        nodes_expanded += 1

        if (r, c) == goal:
            return current_node, nodes_expanded, max_nodes

        directions = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
        for dr, dc in directions:
            if 0 <= dr < rows and 0 <= dc < cols and map_grid[dr][dc] != 0 and (dr, dc) not in visited:
                visited.add((dr, dc))
                queue.append((dr, dc))
                nodes[(dr, dc)] = Node((dr, dc), map_grid[dr][dc], current_node)

    return None, nodes_expanded, max_nodes

def dfs(dimensions, start, goal, map_grid,depth):
    startTime = time.time()
    rows, cols = dimensions
    visited = set()
    stack = deque()
    stack.append(start)
    visited.add(start)
    nodes = {start: Node(start, map_grid[start[0]][start[1]])}
    max_nodes = len(stack)
    nodes_expanded = 0

    while stack:
        elapsed_time = time.time() - startTime
        if elapsed_time > timer:  # 180 seconds = 3 minutes
            print("3-minute time cutoff reached!")
            return None, nodes_expanded, max_nodes
        
        # update max nodes
        max_nodes = max(max_nodes, len(stack))

        # pop a node from stack
        r, c = stack.pop()
        current_node = nodes[(r,c)]
        nodes_expanded += 1

        if (r,c) == goal:
            return current_node, nodes_expanded, max_nodes
        
        if current_node.depth == depth:
            continue

        directions = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
        for dr, dc in directions:
            if 0 <= dr < rows and 0 <= dc < cols and map_grid[dr][dc] != 0 and (dr, dc) not in visited:
                visited.add((dr, dc))
                stack.append((dr, dc))
                nodes[(dr, dc)] = Node((dr, dc), map_grid[dr][dc], current_node)
                new_depth = nodes[(dr, dc)].depth + 1
                nodes[(dr, dc)].depth = new_depth

    return None, nodes_expanded, max_nodes        

#function to read which test case to use
def file_reader():
    try:
        file_name = input("Enter the file name you wish to test: ")
        with open(file_name, 'r') as file:
            dimensions = tuple(map(int, file.readline().split()))
            start = tuple(map(int, file.readline().split()))
            goal = tuple(map(int, file.readline().split()))
            map_grid = [list(map(int, line.split())) for line in file]
            return dimensions, start, goal, map_grid
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None, None, None, None

# function that calls search algos depending on user input
def searchDecision(searchChoice, dimensions, start, goal, map_grid):
    if searchChoice == "bfs":
        start_time = time.time()
        end_node, nodes_expanded, max_nodes = bfs(dimensions, start, goal, map_grid)
    elif searchChoice == "ids":
        depth = 0
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > 180:
                print("3-minute cutoff reached")
                break

            end_node, nodes_expanded, max_nodes = dfs(dimensions, start, goal, map_grid,depth)

            if end_node == None:
                depth += 1
                end_node, nodes_expanded, max_nodes = dfs(dimensions, start, goal, map_grid, depth)
            else:
                break
    elif searchChoice == "a*":
        start_time = time.time()
        end_node, nodes_expanded, max_nodes = a_star(dimensions, start, goal, map_grid)
    else:
        print("Search has not been implemented")
        return
    
    elapsed_time = time.time() - start_time
    results(end_node, nodes_expanded, max_nodes, elapsed_time)



def main():
    global timer
    timer = 180
    dimensions, start, goal, map_grid = file_reader()
    if not dimensions or not start or not goal or not map_grid:
        print("File not in correct format")
        return
    search_choice = input("Enter search algorithm (bfs, ids, a*):")
    searchDecision(search_choice, dimensions, start, goal, map_grid)
    

if __name__ == "__main__":
    main()
