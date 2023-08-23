import sys

input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        answer += 1

    for i in range(4):
        nr = r + dr[(d - i - 1) % 4]
        nc = c + dc[(d - i - 1) % 4]
        if graph[nr][nc] == 0:
            d = (d - i - 1) % 4
            break
    else:
        nr = r - dr[d]
        nc = c - dc[d]
        if graph[nr][nc] == 1:
            break
    r, c = nr, nc


print(answer)
