'''
 - 각 좌표를 방문할 때마다 그룹을 설정해준다
 - 방문했던 좌표를 재방문하게 되면 직전에 방문했던 그룹과 동일하면 이분그래프가 아니다

'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, group):
    global answer
    visited[x] = group
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx, group % 2 + 1)
        elif visited[nx] == group:
            answer = "NO"
           
        
T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    answer = 'YES'
    visited = [0] * (V + 1)
    for _ in range(E):
        u, v  = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    

    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i, 1)
    print(answer)
    