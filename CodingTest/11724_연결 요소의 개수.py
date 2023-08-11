import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)
    

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1
        
print(answer)
    
