from collections import deque
import time



class Node:
    def __init__(self, coord, cost, parent=None):
        self.parent = parent
        self.coord = coord
        self.cost = cost

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
        elapsedTime = time.time() - startTime
        if elapsedTime > 180:  # 180 seconds = 3 minutes
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

def dfs(dimensions, start, goal, map_grid):
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
        elapsedTime = time.time() - startTime
        if elapsedTime > 180:  # 180 seconds = 3 minutes
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
        directions = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
        for dr, dc in directions:
            if 0 <= dr < rows and 0 <= dc < cols and map_grid[dr][dc] != 0 and (dr, dc) not in visited:
                visited.add((dr, dc))
                stack.append((dr, dc))
                nodes[(dr, dc)] = Node((dr, dc), map_grid[dr][dc], current_node)

    return None, nodes_expanded, max_nodes        

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




def main():
    dimensions, start, goal, map_grid = file_reader()
    if not dimensions or not start or not goal or not map_grid:
        return
    searchChoice = input("Enter search algorithm (bfs, ids, a*):")
    if searchChoice == "bfs":
        start_time = time.time()
        end_node, nodes_expanded, max_nodes = bfs(dimensions, start, goal, map_grid)
        end_time = time.time()

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
            print("Total time: {:.9f} seconds".format(end_time - start_time))
            print("Path sequence:", path)
        else:
        
            print("No path found.")
            print("Number of nodes expanded:", nodes_expanded)
            print("Max nodes stored in memory:", max_nodes)
            print("Total time: {:.9f} seconds".format(end_time - start_time))
    if searchChoice == "ids":
        start_time = time.time()
        end_node, nodes_expanded, max_nodes = dfs(dimensions, start, goal, map_grid)
        end_time = time.time()

        if end_node:
            total_cost = 0
            path =[]
            while end_node:
                path.append(end_node.coord)
                total_cost += end_node.cost
                end_node = end_node.parent
            path = path[::-1]
            print("Path Found!")
            print("Total Cost:", total_cost)
            print("Number of nodes expanded:", nodes_expanded)
            print("Max nodes stored in memory:", max_nodes)
            print("Total time: {:.9f} seconds".format(end_time - start_time))
            print("Path sequence:", path)
        else:
            print("No path found.")
            print("Number of nodes expanded:", nodes_expanded)
            print("Max nodes stored in memory:", max_nodes)
            print("Total time: {:.9f} seconds".format(end_time - start_time))
    else:
        print("Search has not been implemented")
    


    

if __name__ == "__main__":
    main()
