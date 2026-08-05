from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

queue = deque([('A', ['A'])])
visited = []

while queue:
    node, path = queue.popleft()

    if node not in visited:
        visited.append(node)

        if node == 'H':
            print("Path:", path)
            print("Visited:", visited)
            break

        for neighbor in graph[node]:
            queue.append((neighbor, path + [neighbor]))