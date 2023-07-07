import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(start):
    queue = deque(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    for g in graph:
        if 0 in g:
            return -1
        
    return max(map(max, graph)) - 1


M, N = map(int, sys.stdin.readline().split())
graph = []
start = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for y in range(M):
        if graph[x][y] == 1:
            start.append((x, y))
            
print(bfs(start))
