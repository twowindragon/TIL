import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(start):
    queue = deque(start)
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    queue.append((nx, ny, nz))
    result = 0
    for gg in graph:
        for g in gg:   
            if 0 in g:
                return -1
            result = max(result, max(g))
    return result - 1


M, N, H = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(H)]
start = []
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for x in range(H):
    for y in range(N):
        graph[x].append(list(map(int, sys.stdin.readline().split())))
        for z in range(M):
            if graph[x][y][z] == 1:
                start.append((x, y, z))

print(bfs(start))