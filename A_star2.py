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
    'B': ['A','C','D','G'],
    'C': ['A','B','D','G'],
    'D': ['A','B','C','G'],
    'E': ['A','G'],
    'F': ['D','G'],
    'G': ['C','D','E','F'],
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
    g = cost[from_node]['g']+g_value(from_node, to_node, algorithm=algo)
    return h+g

algo = Manhattan
start_node = 'A'
goal_node = 'F'
cost = {}

open_list = [start_node]
heap = {}
cost[start_node] = {}
cost[start_node]['h'] = heuristic(start_node, goal_node, algorithm=algo)
cost[start_node]['g'] = g_value(start_node,start_node, algorithm=algo)
heap[start_node] = A_star(start_node, start_node, goal_node, cost)
closed_list = []
N = start_node
successor = []
goal_test = False
parents = {}
parents[start_node] = None
while (len(open_list)):
    print("Open List: ", end = "")
    print(*open_list, sep=" | ")
    # front_node = heappop(open_list)
    mini = float('inf')
    for node,c in heap.items():
        if (c<mini and node not in closed_list):
            mini = c
            front_node = node
    print(front_node)
    index = open_list.index(front_node)
    open_list.pop(index)
    print("N: ", end = "")
    print(front_node)
    print("Closed List: ", end = "")
    print(*closed_list, sep = " | ")
    closed_list.append(front_node)
    if (front_node==goal_node):
        print("Goal Test: True")
        goal_test = True
        break
    print("Goal Test: False")
    for node in graph[front_node]:
        g = cost[front_node]['g']+g_value(front_node,node,algorithm=algo)
        c = A_star(front_node, node, goal_node, cost)
        if (node not in open_list and node not in closed_list):
            h = heuristic(node, goal_node, algorithm=algo)
            parents[node] = front_node
            cost[node] = {}
            cost[node]['h'] = h
            cost[node]['g'] = g
            heap[node] = h+g
            open_list.append(node)
        elif (g<cost[node]['g']):
            parents[node] = front_node
            cost[node]['g'] = g
            heap[node] = h+g
    for par,child in parents.items():
        print(par, child)
    print()

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
