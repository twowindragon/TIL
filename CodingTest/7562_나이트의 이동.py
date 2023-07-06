import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(start, end):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        if (x,y) == end:
            return graph[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

dx = [-1, 1, -1, 1, -2, 2, -2, 2]
dy = [-2, -2, 2, 2, -1, -1, 1, 1]
T = int(sys.stdin.readline())
for _ in range(T):
    I = int(sys.stdin.readline())
    start = tuple(map(int, sys.stdin.readline().split()))
    end = tuple(map(int, sys.stdin.readline().split()))
    graph = [[0] * I for _ in range(I)]
    print(bfs(start, end))
