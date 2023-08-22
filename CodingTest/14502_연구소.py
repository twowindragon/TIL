import sys
import copy
from collections import deque

input = sys.stdin.readline


def bfs(graph):
    q = deque()
    cnt = 0
    for i, j in virus:
        q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))

    for i in range(N):
        cnt += graph[i].count(0)
    return cnt


def dfs(idx, array):
    global answer
    if len(array) == 3:
        temp_graph = copy.deepcopy(graph)
        for x, y in array:
            temp_graph[x][y] = 1
        answer = max(answer, bfs(temp_graph))
        return

    for i in range(idx, N * M):
        if graph[xy[i][0]][xy[i][1]] == 0:
            dfs(i + 1, array + [xy[i]])


N, M = map(int, input().split())
graph = []
aa = []
virus, xy = [], []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 0
for i in range(N):
    graph.append(list(map(int, input().rstrip().split())))
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i, j))
        xy.append((i, j))

dfs(0, [])
print(answer)
