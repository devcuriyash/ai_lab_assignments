# A [25 44]
# B [92 46]
# C [62 69]
# D [82 45]
# E [86  7]
# F [89 27]
# G [59 99]

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

def g_value(from_node, to_node, algorithm=Euclidean):
    return algorithm(locations[from_node], locations[to_node])

def A_star(from_node, to_node, goal_node, cost):
    algo = Euclidean
    h = heuristic(from_node, goal_node, algorithm=algo)
    g = cost[from_node[1]]['g']+g_value(from_node, to_node, algorithm=algo)
    return h+g

start_node = 'A'
goal_node = 'F'
cost = {}

open_list = []
cost[start_node] = {}
cost[start_node]['h'] = heuristic(start_node, goal_node)
cost[start_node]['g'] = g_value(start_node,start_node)
heappush(open_list, (cost[start_node]['h']+cost[start_node]['g'], start_node))
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
    while (front_node in closed_list):
        front_node = heappop(open_list)
    print("N: ", end = "")
    print(front_node[1])
    print("Closed List: ", end = "")
    
    closed_list.append(front_node[1])
    print(*closed_list, sep = " | ")

    # Print successor with heristic
    if (front_node[1]==goal_node):
        print("Goal Test: True")
        goal_test = True
        break
    print("Goal Test: False")
    for node in graph[front_node[1]]:
        c = A_star(front_node[1], node, goal_node, cost)
        if (node not in open_list and node not in closed_list):
            parents[node] = front_node[1]
            cost[node] = {}
            # cost[node]['h'] = h
            # cost[node]['g'] = g
            heappush(open_list, (cost[node]['h']+cost[node]['g'], node))
        elif (g<cost[node]['g']):
            parents[node] = front_node[1]
            cost[node]['g'] = g
            heappush(open_list, (cost[node]['h']+g))
    print()

if not(goal_test):
    print("Path does not exist")
    exit(0)

node = goal_node
print()
print("Path")
print("----")
total_cost = 0
path = []
while (node!=None):
    total_cost += cost[node]['h']+cost[node]['g']
    path.append(node)
    node = parents[node]
print(*path[::-1], sep=" -> ")
print()
print("Total Cost")
print("----------")
print(total_cost)
print()
