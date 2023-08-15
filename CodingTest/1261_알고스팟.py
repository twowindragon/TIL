"""
 - 벽이 아닌경우가 우선이어야되니까 q에 appendleft하자
"""

import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y, 0)])
    visited[x][y] = True

    while q:
        x, y, cnt = q.popleft()
        if x == N - 1 and y == M - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.appendleft((nx, ny, cnt))

                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))


M, N = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
print(bfs(0, 0))
