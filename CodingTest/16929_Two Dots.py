'''
 - 방문했던 곳을 재방문하는 경우에서 직전 방문 경우의 수만 제외해주면 된다.
'''

import sys
input = sys.stdin.readline


def dfs(x, y, pre, cnt):
    global answer
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if not visited[x][y] and pre == graph[x][y]:
        visited[x][y] = cnt
        dfs(x, y + 1, pre, cnt + 1)
        dfs(x + 1, y, pre, cnt + 1)
        dfs(x, y - 1, pre, cnt + 1)
        dfs(x - 1, y, pre, cnt + 1)
    elif visited[x][y] and cnt - visited[x][y] >= 3:
        answer = 'Yes'
        return 
           
    
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

answer = 'No'
for i in range(N):
    for j in range(M):
        visited = [[0] * M for _ in range(N)]
        dfs(i, j, graph[i][j], 1)
        if answer == 'Yes':
            print(answer)
            exit()
print(answer)

########################### 남이 푼 답안 
import sys
input=sys.stdin.readline
n,m = map(int,input().split())
ary = [list(input()) for _ in range(n)]
dx=[1,0,0,-1]
dy=[0,1,-1,0]
visited = [[0 for _ in range(m)] for __ in range(n)]
result=[]
def dfs(x,y,prex,prey,cnt):
    if visited[x][y] and cnt >=4:
        result.append("yes")
        return
    visited[x][y]=1
    for idx in range(4):
        nx = dx[idx]+x
        ny = dy[idx]+y
        if 0<=nx<n and 0<=ny<m and ary[nx][ny]==ary[x][y]:
            if [nx,ny]!=[prex,prey]:
                dfs(nx,ny,x,y,cnt+1)


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j,i,j,0)
if result:
    print("Yes")
else:
    print("No")