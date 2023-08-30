# Create the graph
# Make an adjacency list
# State space
# -----------
# 0 1 0 0 0 1
# 0 0 1 1 1 0
# 1 1 0 0 0 0
# 0 0 0 0 0 1
# 0 1 0 1 0 0
# 0 0 1 0 1 0

graph = {
    0: [1,5],
    1: [2,3,4],
    2: [0,1],
    3: [5],
    4: [1,3],
    5: [2,4]
}

def traverse(start, end):
    visited = {}
    nodes = []
    if (graph.get(start)==None):
        print()
        print("Node not in graph")
        print()
        return
    if (dfs(start, end, visited, nodes)):
        print()
        print(*nodes, sep=' -> ')
        print()
    else:
        print("Unreachable")

def dfs(node_val, end, visited, nodes):
    if node_val not in visited:
        visited[node_val] = True
        nodes.append(node_val)
        if (node_val==goal):
            return True
        for neighbor in graph.get(node_val, []):
            if (dfs(neighbor, end, visited, nodes)):
                return True
    return False

def options_menu():
    print("Options")
    print("-------")
    i = 0
    print(f"{i}. Exit")
    i+=1
    print(f"{i}. DFS")
    i+=1

while (True):
    options_menu()
    option = input("Enter option: ")
    if (option=='1'):
        start = int(input("Enter start node: "))
        goal = int(input("Enter goal node: "))
        traverse(start, goal)
    if (option=='0'):
        break
