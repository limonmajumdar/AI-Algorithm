def best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start)]
    visited = set()
    parent = {}
    parent[start] = None
    
    while priority_queue:
        priority_queue.sort()
        current_cost, current_node = priority_queue.pop(0)
        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                priority_queue.append((heuristic[neighbor], neighbor))
                parent[neighbor] = current_node
    
    return None

graph = {
    'S': [('B', 11), ('C', 14), ('D', 7)],
    'B': [('E', 15)],
    'C': [('E', 8), ('F', 10)],
    'D': [('F', 25)],
    'E': [('H', 4)],
    'F': [('G', 20)],
    'H': [('G', 10)],
    'G': []
}

heuristic = {
    'S': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0
}

start_node = 'S'
goal_node = 'G'
path = best_first_search(graph, start_node, goal_node, heuristic)

if path:
    print("\nPath found:", path)
else:
    print("\nNo path could be found.")