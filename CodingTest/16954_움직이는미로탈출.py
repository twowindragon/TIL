"""
 - 제의 캐릭터가 먼저 이동하고, 그 다음 벽이 이동
 -  벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다
 - *** 방문체크를 그래프가 변하지않는 1초안에서만 수행
"""
from collections import deque
import copy


def bfs(graph):
    q = deque([(N - 1, 0)])
    while q:
        visited = [[False] * N for _ in range(N)]
        temp_graph = copy.deepcopy(graph)
        temp_graph[1:] = temp_graph[:-1]
        temp_graph[0] = ["."] * N
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == 0 and y == N - 1:
                return 1
            if graph[x][y] == "#":
                continue
            
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if (
                        graph[nx][ny] == "."
                        and not visited[nx][ny]
                        and temp_graph[nx][ny] != "#"
                    ):
                        visited[nx][ny] = True
                        q.append((nx, ny))
        graph = copy.deepcopy(temp_graph)

    return 0


N = 8
visited = [[0] * N for _ in range(N)]
graph = [list(input()) for _ in range(N)]
dx = [-1, 0, 1, 0, -1, 1, -1, 1, 0]
dy = [0, -1, 0, 1, -1, -1, 1, 1, 0]
print(bfs(graph))
