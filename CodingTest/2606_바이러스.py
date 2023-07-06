import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    visited[x] = True
    for next in graph[x]:
        if not visited[next]:
            dfs(next)

dfs(1)

print(sum(visited) - 1)
