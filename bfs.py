from queue import PriorityQueue

# Define the graph connections
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

# Define heuristic values (estimated cost to reach the goal)
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 6,
    'F': 2,
    'G': 1
}

def best_first_search(start, goal):
    visited = set()  # Keep track of visited nodes
    pq = PriorityQueue()  # Priority queue for sorting by heuristic value
    pq.put((heuristic[start], start))  # (priority, node)

    while not pq.empty():
        _, current = pq.get()
        if current in visited:
            continue
        
        print("Visiting:", current)
        visited.add(current)

        if current == goal:
            print("Goal reached:", goal)
            return
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

# Run the search
best_first_search('A', 'G')
