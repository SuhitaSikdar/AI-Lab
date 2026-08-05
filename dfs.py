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

stack = [('A', ['A'])]

while stack:
    node, path = stack.pop()

    if node == 'H':
        print("Path:", path)
        break

    for neighbor in reversed(graph[node]):
        stack.append((neighbor, path + [neighbor]))