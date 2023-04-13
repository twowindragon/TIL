import sys
import copy
input = sys.stdin.readline
R, C, T = map(int, input().split())
graph = []
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
a = []
b = []


for i in range(R):
    graph.append(list(map(int, input().split())))
    for j in range(C):
        if graph[i][j] == -1:
            clean_x_up, clean_y = i - 1, j - 1
clean_x_down = clean_x_up + 1

for r in range(clean_x_up - 1, -1, -1):
    a.append((r, 0))
for c in range(1, C):
    a.append((0, c))
for r in range(1, clean_x_up):
    a.append((r, C - 1))
for c in range(C - 1, 0, -1):
    a.append((clean_x_up, c))

for r in range(clean_x_down + 1, R):
    b.append((r, 0))
for c in range(1, C - 1):
    b.append((R - 1, c))
for r in range(R - 1, clean_x_down - 1, -1):
    b.append((r, C - 1))
for c in range(C - 2, 0, -1):
    b.append((clean_x_down, c))


for t in range(T):
    temp_graph = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                cnt = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                        temp_graph[nr][nc] += (graph[r][c] // 5)
                        cnt += 1
                graph[r][c] -= (graph[r][c] // 5 * cnt)

    for r in range(R):
        for c in range(C):
            if temp_graph[r][c] != 0:
                graph[r][c] += temp_graph[r][c]

    for i in range(len(a)):
        if i == len(a) - 1:
            graph[a[i][0]][a[i][1]] = 0
            continue
        graph[a[i][0]][a[i][1]] = graph[a[i + 1][0]][a[i + 1][1]]

    for i in range(len(b)):
        if i == len(b) - 1:
            graph[b[i][0]][b[i][1]] = 0
            continue
        graph[b[i][0]][b[i][1]] = graph[b[i + 1][0]][b[i + 1][1]]

ans = 0
for i in range(R):
    for j in range(C):
        ans += graph[i][j]

print(ans + 2)
