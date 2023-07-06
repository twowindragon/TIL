import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] += 1
    while queue:
        (x, y) = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[N - 1][M - 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


N, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * M for _ in range(N)]
graph = [list(map(int, input())) for _ in range(N)]

print(bfs(0, 0))