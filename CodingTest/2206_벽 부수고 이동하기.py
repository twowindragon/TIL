import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(x, y):
    dist = [[[0] * M for _ in range(N)] for _ in range(2)]
    queue = deque([(1, x, y)])
    dist[1][x][y] = 1
    while queue:
        wall, x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            return dist[wall][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and wall == 1 and dist[wall - 1][nx][ny] == 0:
                    dist[wall - 1][nx][ny] = dist[wall][x][y] + 1
                    queue.append((0, nx, ny))

                if graph[nx][ny] == 0 and dist[wall][nx][ny] == 0:
                    dist[wall][nx][ny] = dist[wall][x][y] + 1
                    queue.append((wall, nx, ny))

    return -1


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))
