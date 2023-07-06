import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()


def bfs(x):
    cnt = 1
    visited[x] = cnt
    queue = deque([x])
    while queue:
        x = queue.popleft()
        for next in graph[x]:
            if visited[next] == 0:
                cnt += 1
                visited[next] = cnt
                queue.append(next)


bfs(R)
for i in range(1, N + 1):
    print(visited[i])
