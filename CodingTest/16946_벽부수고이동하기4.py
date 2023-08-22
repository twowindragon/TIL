import sys
import copy
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])

    visited[x][y] = True
    wall = set()
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

                if graph[nx][ny] == 1:
                    wall.add((nx, ny))

    for x, y in wall:
        answer[x][y] += cnt

    return


N, M = map(int, input().split())
graph = []
walls = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    graph.append(list(map(int, input().rstrip())))
    for j in range(M):
        if graph[i][j] == 1:
            walls.append((i, j))

answer = copy.deepcopy(graph)

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 0:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        print(answer[i][j] % 10, end="")
    print()
