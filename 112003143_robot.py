import colorama
from colorama import Fore
import numpy as np

grid = np.zeros((10,10), dtype=int)

obstacles = [[1,2],[2,2],[3,2],[4,2],[4,3],[4,4],
             [1,5],[1,6],[1,7],[1,8],[2,6],
             [4,7],[5,7],[6,7],[7,7],[7,5],[7,6],[7,8],
             [6,1],[6,2],[6,3],[7,3],[8,3]]

for o in obstacles:
    grid[o[0]][o[1]] = 1

for i in range(10):
    print(grid[i])
print()

start_node = np.array([7,2])
end_node = np.array([8,4])

# Cost is taken as steps from start/number of active neighbors
# For beginning, let's just do steps from the start, so this
# becomes an equal step cost

# Need a cost matrix and a heuristic matrix
Euclidean = lambda A,B: sum((A-B)**2)**0.5
Manhattan = lambda A,B: sum(abs(A-B))
heuristicAlgo = Manhattan

def heuristic(node, goal_node, algorithm=Manhattan):
    return algorithm(node, goal_node)

def g(node):
    return node[1]

def f(parent, curr_node, goal_node, algo="UCS"):
    # cur_node = [[x, y], steps, parent]
    if (algo=="UCS"):
        # f(n) = g(n)
        # Find the current step cost and add it
        return g(parent)+1
    elif algo=="Best First":
        # f(n) = h(n)
        # print(curr_node, goal_node, heuristic(curr_node, goal_node, algorithm=heuristicAlgo))
        return heuristic(curr_node, goal_node, algorithm=heuristicAlgo)
    elif algo=="A Star":
        # f(n) = h(n) + g(n)
        return g(parent)+1 + heuristic(curr_node, goal_node, algorithm=heuristicAlgo)

def DisplayGrid(grid, row, col):
    for i in range(10):
        for j in range(10):
            if (i==row and j==col):
                print(Fore.RED + f"{grid[i][j]}", end = " ")
            else:
                print(Fore.WHITE + f"{grid[i][j]}", end = " ")
        print()
    print(Fore.WHITE)

def add_neighbors(heap, front, open_list, successors, algo="UCS"):
    row = front[0][0]
    col = front[0][1]
    grid[row][col] = 2
    steps = front[1]

    # Up
    for x in range(-1, 3, 2):
        if (row+x>=0 and row+x<10) and grid[row+x][col]==0:
            f_n = f(front, np.array([row+x,col]), end_node, algo=algo)
            elem = heap.get(tuple([row+x,col]), None)
            heap[tuple([row+x,col])] = [f_n, front[0]]
            successors.append(np.array([row+x,col]))
            if elem==None:
                open_list.append(np.array([row+x,col]))
        elif (row+x>=0 and row+x<10 and grid[row+x][col]==2):
            f_n = f(front, np.array([row+x,col]), end_node, algo=algo)
            val = heap.get(tuple([row+x, col]), None)
            if val!=None and f_n<val[0]:
                # Update
                heap[tuple([row+x,col])] = [f_n, front[0]]
                successors.append(np.array([row+x,col]))
    
    for y in range(-1, 3, 2):
        if (col+y>=0 and col+y<10) and grid[row][col+y]==0:
            f_n = f(front, np.array([row,col+y]), end_node, algo=algo)
            elem = heap.get(tuple([row,col+y]), None)
            heap[tuple([row,col+y])] = [f_n, front[0]]
            successors.append(np.array([row,col+y]))
            if elem==None:
                open_list.append(np.array([row,col+y]))
        elif (col+y>=0 and col+y<10 and grid[row][col+y]==2):
            f_n = f(front, np.array([row,col+y]), end_node, algo=algo)
            val = heap.get(tuple([row, col+y]), None)
            if val!=None and f_n<val[0]:
                # Update
                heap[tuple([row,col+y])] = [f_n, front[0]]
                successors.append(np.array([row,col+y]))
    
def generate_heading(string):
    print(string)
    print("-"*len(string))

# algo = "UCS"
# algo = "Best First"
algo = "A Star"
start_cost = 0
if (algo=="Best First" or algo=="A Star"):
    start_cost = heuristic(start_node, end_node)
print(start_cost)

heap = {tuple([start_node[0], start_node[1]]): [start_cost, np.array([None,None])]}
parents = {}
open_list = [start_node]
closed_list = []
while len(open_list):
    # Find the minimum
    mini = float('inf')
    index = 0

    # Open list
    generate_heading("Open list")

    for i in range(len(open_list)):
        n = open_list[i]
        c = heap[tuple([n[0], n[1]])]
        if (c[0]<mini and grid[n[0]][n[1]]==0):
            mini = c[0]
            front = [np.array(n), c[0], c[1]]
            index = i
        print(n, c[0], end = " --- ")
    print("\n")
    closed_list.append(open_list[index])
    del open_list[index]

    # N
    print(f"N: {front[0]}")
    print()
    
    # Closed list
    generate_heading("Closed list")
    print(*closed_list, sep=" ")

    parents[tuple([front[0][0], front[0][1]])] = front[2]
    
    # Path
    print()
    generate_heading("Path")
    node = front[0]
    path = []
    while (node!=np.array([None,None])).all():
        key = tuple([node[0], node[1]])
        path.append([node, heap[key][0]])
        node = parents[tuple([node[0], node[1]])]
    N = len(path)
    for i in range(N-1, -1, -1):
        print(path[i][0], path[i][1], end = " -> ")
    print()

    if (front[0]==end_node).all():
        print()
        break

    # Successors
    successors = []
    add_neighbors(heap, front, open_list, successors, algo=algo)
    print()
    generate_heading("Successors")
    for succ in successors:
        print(np.ravel(succ), heap[tuple([succ[0], succ[1]])][0], end=" --- ")
    print()
    print("="*21)

node = end_node

path = np.zeros((10,10), dtype=int)
while (node!=np.array([None,None])).all():
    # print(node)
    path[node[0]][node[1]] = 1
    node = parents[tuple([node[0], node[1]])]

for i in range(10):
    for j in range(10):
        if (np.array([i,j])==start_node).all():
            print(Fore.YELLOW + f"{path[i][j]}", end = " ")
            continue
        if (np.array([i,j])==end_node).all():
            print(Fore.BLUE + f"{path[i][j]}", end = " ")
            continue
        if [i,j] in obstacles:
            print(Fore.RED + f"{path[i][j]}", end=" ")
            continue
        if path[i][j]==1:
            print(Fore.GREEN + f"{path[i][j]}", end=" ")
        else:
            print(Fore.WHITE + f"{path[i][j]}", end = " ")
    print()

# print(path)
