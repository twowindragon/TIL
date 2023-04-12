from collections import deque


def bfs(x, y, size):
    visited = [[0] * N for _ in range(N)]
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if 1<= graph[x][y] <=6 and graph[x][y] < size :
            for i, j in fish:
                if graph[i][j] < size and visited[i][j] == visited[x][y]:
                    if i < x:
                        x, y = i, j
                    elif x == i and j < y:
                        x, y = i, j

            graph[x][y] = 0
            fish.remove((x, y))
            graph[shark_x][shark_y] = 0
            return 1, x, y, visited[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return 0, x, y, visited[x][y] - 1

N = int(input())
ans = 0
graph = []
fish = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
        elif graph[i][j] != 0:
            fish.append((i, j))

size = 2
level_up = 0
while True:
    eat, shark_x, shark_y, cnt = bfs(shark_x, shark_y, size)
    if eat == 0:
        break
    level_up += eat
    ans += cnt
    if level_up == size:
        size += 1
        level_up = 0

print(ans)