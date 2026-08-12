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

pq = [(h['S'], 0, 'S', ['S'])]

while pq:
    f, g, node, path = heapq.heappop(pq)

    if node == 'G':
        print("Path:", path)
        print("Cost:", g)
        break

    for neighbor, cost in graph[node]:
        new_g = g + cost
        new_f = new_g + h[neighbor]

        heapq.heappush(
            pq,
            (new_f, new_g, neighbor, path + [neighbor])
        )