import heapq

graph = {
    'S': [('A', 2), ('B', 1)],
    'A': [('G', 10)],
    'B': [('G', 4)],
    'G': []
}

h = {
    'S': 4,
    'A': 2,
    'B': 3,
    'G': 0
}

# (heuristic, current_node, path, total_cost)
frontier = [(h['S'], 'S', ['S'], 0)]

while frontier:
    _, node, path, cost = heapq.heappop(frontier)

    if node == 'G':
        print("Path:", " → ".join(path))
        print("Cost:", cost)
        break

    for neighbor, road_cost in graph[node]:
        new_cost = cost + road_cost

        heapq.heappush(
            frontier,
            (h[neighbor], neighbor, path + [neighbor], new_cost)
        )