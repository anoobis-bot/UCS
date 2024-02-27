def ucs(graph, start, goal):
    explored = set()
    frontier = [(0, start, [])]  # (cost, node, path)

    while frontier:
        frontier.sort(key=lambda x: x[0])  # Sort frontier by cost
        cost, current_node, path = frontier.pop(0)  # Get the lowest cost node

        if current_node in explored:
            continue

        if current_node in goal:
            # Goal node reached, return the path
            return path + [current_node], cost

        explored.add(current_node)

        for neighbor, edge_cost in graph[current_node]:
            if neighbor not in explored:
                new_cost = cost + edge_cost
                new_path = path + [current_node]
                frontier.append((new_cost, neighbor, new_path))

    # If no path is found
    return None


def load_graph(graph, path):
    with open(path) as file:
        for line in file:
            key, unclean_nodes = line.split(" : ")
            graph[key] = []
            unclean_nodes = unclean_nodes.replace('(', '')
            unclean_nodes = unclean_nodes.replace(')', '')
            nodes = unclean_nodes.split()
            for node in nodes:
                key_node, value_node = node.split(",")
                graph[key].append((key_node, int(value_node)))


repeat = True

while repeat:
    graph = {}

    path = input("Enter path of graph file: ")

    load_graph(graph, path)

    start_node = input("Enter the start node: ")

    goal_nodes = []
    while True:
        goal = input("Enter a goal node (or 'done' if finished): ")
        if goal == 'done':
            break
        goal_nodes.append(goal)

    try:
        # Run UCS algorithm with user-defined graph, start node, and goal nodes
        result, total_cost = ucs(graph, start_node, goal_nodes)
        print("Optimal path:", "->".join(result))
        print("Total cost:", total_cost)
    except TypeError:
        print("No path found.")

    input_repeat = input("do you want to repeat? (Y/N) ")
    if input_repeat == 'N':
        repeat = False
    print("\n")
