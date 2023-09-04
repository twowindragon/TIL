"""
 - 각 cctv를 모든 방향에 대해 시행해서 사각지대 최소값 구하기
 - cctv리스트에  cctv들의 좌표랑 종류를 저장
 - 이 리스트에 대해 포문을 돌려 1, 3, 4는 3번 2는 1번 5 는 0번 회전
"""
import copy


def dfs(n, graph):
    global answer
    if n == len(cctv):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    cnt += 1
        answer = min(answer, cnt)

        return
    x, y, num = cctv[n]

    for j in range(len(num_direction[num])):
        temp_graph = copy.deepcopy(graph)

        for k in range(len(num_direction[num][j])):
            idx = num_direction[num][j][k]
            nx, ny = x, y
            while temp_graph[nx][ny] != 6:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = "#"
                nx = nx + dx[idx]
                ny = ny + dy[idx]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
        dfs(n + 1, temp_graph)


N, M = map(int, input().split())
graph = []
cctv = []
answer = N * M
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
num_direction = {
    1: [(0,), (1,), (2,), (3,)],
    2: [(0, 2), (1, 3)],
    3: [(0, 1), (1, 2), (2, 3), (3, 0)],
    4: [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)],
    5: [(0, 1, 2, 3)],
}
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 0 or graph[i][j] == 6:
            continue
        cctv.append((i, j, graph[i][j]))

dfs(0, graph)
print(answer)
