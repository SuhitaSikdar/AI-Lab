import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('C', 2)],
    'C': [('D', 1)],
    'D': []
}

pq = [(0, 'A', ['A'])]

while pq:
    cost, node, path = heapq.heappop(pq)

    if node == 'D':
        print("Cheapest Path:", path)
        print("Minimum Cost:", cost)
        break

    for next_node, edge_cost in graph[node]:
        new_cost = cost + edge_cost
        new_path = path + [next_node]

        heapq.heappush(pq, (new_cost, next_node, new_path))