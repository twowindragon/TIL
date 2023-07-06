import sys
# sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**9)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()


def dfs(x):
    global cnt
    visited[x] = cnt
    for next in graph[x]:
        if visited[next] == 0:
            cnt += 1
            dfs(next)


cnt = 1
dfs(R)
for i in range(1, N + 1):
    print(visited[i])
