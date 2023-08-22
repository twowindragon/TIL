from collections import deque


def check_size(x, y, z):  # 큰 순서대로 return
    temp = sorted([x, y, z])
    return temp[2], temp[1], temp[0]


def bfs(x, y, z):
    if (x + y + z) % 3 != 0:
        return 0
    x, y, z = check_size(x, y, z)
    q = deque([(x, y, z)])
    visited.add((x, y, z))
    while q:
        a, b, c = q.popleft()
        if a == b == c:
            return 1
        a, b, c = check_size(a, b, c)  # a >= b >= c
        if a != b:
            na = a - b
            nb = b + b
            temp = tuple(sorted((na, nb, c), reverse=True))
            if temp not in visited:
                visited.add(temp)
                q.append(temp)
        if a != c:
            na = a - c
            nc = c + c
            temp = tuple(sorted((na, b, nc), reverse=True))
            if temp not in visited:
                visited.add(temp)
                q.append(temp)
        if b != c:
            nb = b - c
            nc = c + c
            temp = tuple(sorted((a, nb, nc), reverse=True))
            if temp not in visited:
                visited.add(temp)
                q.append(temp)
    return 0


A, B, C = map(int, input().split())
visited = set()
print(bfs(A, B, C))
