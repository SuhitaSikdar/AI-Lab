from collections import deque

def successors(s):
    x, y = s
    r = set()

    r.add((4, y))          # Fill X
    r.add((x, 3))          # Fill Y
    r.add((0, y))          # Empty X
    r.add((x, 0))          # Empty Y

    t = min(x, 3 - y)      # X -> Y
    r.add((x - t, y + t))

    t = min(y, 4 - x)      # Y -> X
    r.add((x + t, y - t))

    return r

start = (0, 0)

visited = {start}
q = deque([start])

level = 0

while q:
    size = len(q)
    new_states = 0

    for _ in range(size):
        state = q.popleft()

        for nxt in successors(state):
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
                new_states += 1

    print("Level", level, "added", new_states, "states")
    level += 1

print("Total states =", len(visited))