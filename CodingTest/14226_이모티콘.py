'''
 - 클립보드 변수가 필요한가? -> 계속 변하니까 큐에 넣어서?
 - 
'''
from collections import deque

def bfs(x):
    q = deque([(x, 0)])
    visited[x][0] = 1
    while q:
        x, clip = q.popleft()
        if x == S:
            
            return visited[x][clip]
        
        if not visited[x][x]:
            visited[x][x] = visited[x][clip] + 1
            q.append((x, x))
            
        for nx in [x + clip, x - 1]:
            if 2 <= nx <= 1000 and not visited[nx][clip]:
                visited[nx][clip] = visited[x][clip] + 1
                q.append((nx, clip))
        
        
      
S = int(input())
visited = [[0] * 1001 for _ in range(1001)]
print(bfs(1) - 1)