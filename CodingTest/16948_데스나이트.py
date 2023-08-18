from collections import deque


def bfs():
    q = deque([(start_x, start_y, 0)])
    visited.add((start_x, start_y))
    while q:
        x, y, cnt = q.popleft()
        if x == end_x and y == end_y:
            return cnt

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, cnt + 1))
    return -1


N = int(input())
start_x, start_y, end_x, end_y = map(int, input().split())
visited = set()
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
print(bfs())
