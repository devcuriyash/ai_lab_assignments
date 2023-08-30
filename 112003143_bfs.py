# Create the graph
# Make an adjacency list
# State Space
# -----------
# 0 0 1 0 1 1 1
# 0 0 1 1 0 0 0
# 0 0 0 0 0 1 0
# 1 0 0 0 0 0 0
# 0 0 0 1 0 0 0
# 0 0 1 0 1 0 0
# 0 1 0 1 0 1 0

graph = {
    0: [2,4,5,6],
    1: [3,4],
    2: [5],
    3: [0],
    4: [3],
    5: [2,4],
    6: [1,3,5]
}

def bfs(start, goal):
    if (graph.get(start)==None):
        print()
        print("Start node not in graph")
        print()
        return
    
    open_list = []
    closed_list = []
    N = None
    goal_test = False
    open_list.append(start)
    N = start
    parents = {start: None}
    
    if (start==goal):
        goal_test = True
    print()
    while (len(open_list) and not(goal_test)):
        print("Open list: ", end="")
        print(*open_list, sep=", ")
        N = open_list.pop()
        if (N==goal):
            goal_test = True
        print(f"N: {N}")
        print("Closed list: ", end="")
        print(*closed_list, sep=", ")
        print(f"Goal test: {goal_test}")
        closed_list.append(N)
        successor = []
        for neighbor in graph.get(N, []):
            if (neighbor not in open_list and neighbor not in closed_list):
                open_list.insert(0, neighbor)
                parents[neighbor] = N
                successor.append(neighbor)
        print("Successor: ", end="")
        print(*successor, sep=", ")
        print()
    if (not(goal_test)):
        print()
        print("Unreachable")
        print()
        return
    p = goal
    nodes = []
    while (p!=None):
        nodes.append(p)
        p = parents[p]
    print(*nodes[::-1], sep=" -> ")
    print()

def options_menu():
    print("Options")
    print("-------")
    i = 0
    print(f"{i}. Exit")
    i+=1
    print(f"{i}. BFS")
    i+=1

while (True):
    options_menu()
    option = input("Enter option: ")
    if (option=='1'):
        start = int(input("Enter start node: "))
        goal = int(input("Enter goal node: "))
        bfs(start, goal)
    if (option=='0'):
        break
