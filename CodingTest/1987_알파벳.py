import sys

input = sys.stdin.readline


def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in alpha:
            alpha.add(graph[nx][ny])
            dfs(nx, ny, cnt + 1)
            alpha.remove(graph[nx][ny])
            
R, C = map(int, input().split())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 0
for _ in range(R):
    graph.append(list(input().rstrip()))
alpha = {graph[0][0]}
dfs(0, 0, 1)
print(answer)
