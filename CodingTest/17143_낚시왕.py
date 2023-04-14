import sys
input = sys.stdin.readline


def shark_move():
    temp_graph = [[0] * C for _ in range(R)]
    cnt = 0
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 0:
                continue
            cnt += 1
            s, d, z = graph[r][c]
            nr, nc, ns = r, c, s
            while s > 0:
                nr += dr[d]
                nc += dc[d]
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    nr -= dr[d]
                    nc -= dc[d]

                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    else:
                        d = 2
                else:
                    s -= 1

            if temp_graph[nr][nc] != 0:
                if temp_graph[nr][nc][2] < z:
                    temp_graph[nr][nc] = (ns, d, z)
            else:
                temp_graph[nr][nc] = (ns, d, z)

    return cnt, temp_graph


R, C, M = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
graph = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r - 1][c - 1] = (s, d - 1, z)

ans = 0

for i in range(C):
    for r in range(R):
        if graph[r][i] != 0:
            ans += graph[r][i][2]
            graph[r][i] = 0
            break

    cnt, graph = shark_move()
    if cnt == 0:
        break

print(ans)
