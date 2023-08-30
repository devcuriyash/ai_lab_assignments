# Define the problem
# Define a heuristic - cost to reach goal node
import numpy as np
from heapq import heappush, heappop
num_nodes = 8
locations = {}
for i in range(65, 65+num_nodes):
    locations[chr(i)] = np.ravel(np.random.randint(100,size=(1,2)))

for loc, pos in locations.items():
    print(loc, pos)

graph = {'A': ['B','C','D','E'],
    'B': ['A','C','D'],
    'C': ['A','B','D','G'],
    'D': ['A','B','C','F','G'],
    'E': ['A'],
    'F': ['D'],
    'G': ['C','D'],
    'H': []
}
print()

Euclidean = lambda A,B: sum((A-B)**2)**0.5
Manhattan = lambda A,B: sum(abs(A-B))

def heuristic(node, goal_node, algorithm=Euclidean):
    return algorithm(locations[node], locations[goal_node])

algo = Manhattan
start_node = 'A'
goal_node = 'F'

open_list = []
heappush(open_list, (heuristic(start_node, goal_node, algorithm=algo), start_node))
closed_list = []
N = start_node
successor = []
goal_test = False
parents = {}
parents[start_node] = None
while (len(open_list)):
    print("Open List: ", end = "")
    print(*open_list, sep=" | ")
    front_node = heappop(open_list)
    print("N: ", end = "")
    print(front_node[1])
    print("Closed List: ", end = "")
    print(*closed_list, sep = " | ")
    closed_list.append(front_node[1])
    if (front_node[1]==goal_node):
        print("Goal Test: True")
        goal_test = True
        break
    print("Goal Test: False")
    for node in graph[front_node[1]]:
        if (node not in open_list and node not in closed_list):
            parents[node] = front_node[1]
            heappush(open_list, (heuristic(node, goal_node,algorithm=algo), node))
    print()

if not(goal_test):
    print("Path does not exist")
    exit(0)

node = goal_node
print()
print("Path")
print("----")
path = []
total_cost = 0
while (node!=None):
    total_cost += heuristic(node, goal_node,algorithm=algo)
    path.append(node)
    node = parents[node]
print(*path[::-1], sep=" -> ")
print()
print("Total Cost")
print("----------")
print(total_cost)
