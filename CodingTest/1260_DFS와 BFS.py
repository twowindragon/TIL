import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, M, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  i,j = map(int, sys.stdin.readline().split())
  graph[i].append(j)
  graph[j].append(i)

for g in graph:
    g.sort()

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v, end= ' ')
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)