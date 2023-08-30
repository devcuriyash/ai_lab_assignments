import copy

class Graph:
    def __init__(self):
        self.__graph = {}
    
    def add_edge(self, from_node, to_node):
        if (from_node not in self.__graph):
            self.__graph[from_node] = []
        self.__graph[from_node].append(to_node)
    
    def get_nodes(self, node):
        return self.__graph[node]
    
    def print_graph(self):
        for node,children in self.__graph.items():
            print(node, children)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 4)
g.add_edge(1, 3)
g.add_edge(1, 5)
g.add_edge(2, 6)
g.add_edge(4, 5)

def IDDFS(graph, root, goal, depth_limit):
    for depth in range(0, depth_limit+1):
        if DFS(graph, root, goal, depth, []):
            return True
    return False

def DFS(graph, root, goal, depth, path):
    path.append(root)
    if (root==goal):
        print(*path, sep=' -> ')
        return True
    if depth==0:
        return False
    for i in graph.get_nodes(root):
        if (DFS(graph, i, goal, depth-1, copy.deepcopy(path))):
            return True
    return False

def options_menu():
    print("Options")
    print("-------")
    i = 0
    print(f"{i}. Exit")
    i+=1
    print(f"{i}. IDDFS")
    i+=1

while (True):
    options_menu()
    option = input("Enter option: ")
    if (option=='1'):
        start = int(input("Enter start node: "))
        goal = int(input("Enter goal node: "))
        depth = int(input("Enter maximum depth: "))
        print()
        if IDDFS(g, start, goal, depth):
            print(f"There exists a path from {start} to {goal} of depth atleast {depth}")
        else:
            print(f"There does not exist a path from {start} to {goal} of depth atleast {depth}")
        print()
    if (option=='0'):
        break
