"""
 - 낮
"""
import sys
from collections import deque


def bfs():
    q = deque([(0, 0, K)])
    visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
    day = 1
    visited[K][0][0] = 1
    ans = 1
    while q:
        for _ in range(len(q)):
            x, y, wall = q.popleft()
            if x == N - 1 and y == M - 1:
                return ans
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 0 and not visited[wall][nx][ny]:
                        visited[wall][nx][ny] = visited[wall][x][y] + 1
                        q.append((nx, ny, wall))
                    if graph[nx][ny] == 1 and wall and not visited[wall - 1][nx][ny]:
                        if day == 1:
                            visited[wall - 1][nx][ny] = visited[wall][x][y] + 1
                            q.append((nx, ny, wall - 1))
                        else:
                            q.append((x, y, wall))
        ans += 1
        day = (day + 1) % 2
    return -1


input = sys.stdin.readline
N, M, K = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
graph = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs())
