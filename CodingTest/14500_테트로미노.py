'''
전부 4개의 도형 ㅜ -> 이 도형만 예외처리
dfs 사용 
매 칸에서 4방향으로 4칸 이동(사실은 아님)
'''
def dfs(x, y, visit, cnt):
    global answer
    if answer >= max_num * (4 - len(visit)) + cnt:
        return
    
    if len(visit) == 4:
        answer = max(answer, cnt)
        return 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if (nx, ny) not in visit:
                dfs(nx, ny, visit + [(nx, ny)], cnt + graph[nx][ny])
                if len(visit) == 2:
                    dfs(x, y, visit + [(nx, ny)], cnt + graph[nx][ny])

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 0
max_num = max(map(max, graph))

for i in range(N):
    for j in range(M):
        dfs(i, j, [(i, j)], graph[i][j])

print(answer)