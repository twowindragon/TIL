import sys


def dfs(x, cnt):
  
    if cnt == 4:
        return 1

    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            if dfs(nx, cnt + 1) == 1:
                return 1
            visited[nx] = False
    return 0
    
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited[i] = True
    ans = dfs(i, 0)
    visited[i] = False
    if ans:
        break
                
print(ans)