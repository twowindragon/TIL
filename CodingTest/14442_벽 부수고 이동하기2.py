'''
 - visit을 set으로 하면 시간초과.. 벽부수기 1이랑 동일
 - pypy3로 제출해야함
'''
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque([(K, 0, 0)])
    visited[K][0][0] = 1
    while q:
        wall, x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[wall][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and not visited[wall][nx][ny]:
                    q.append((wall, nx, ny))
                    visited[wall][nx][ny] = visited[wall][x][y] + 1

                elif graph[nx][ny] == 1 and wall and not visited[wall - 1][nx][ny]:
                    q.append((wall - 1, nx, ny))
                    visited[wall - 1][nx][ny] = visited[wall][x][y] + 1

    return -1


N, M, K = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
print(bfs())
