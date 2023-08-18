"""
 - 둘다 떨어지면 안되고, 둘다벽이면 안되고, 
"""
from collections import deque
import sys

input = sys.stdin.readline


def check(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return -1
    if graph[x][y] == "#":
        return 0
    return 2


def bfs():
    q = deque([(*coins[0], *coins[1], 0)])
    visited.add((*coins[0], *coins[1]))
    while q:
        coin1_x, coin1_y, coin2_x, coin2_y, cnt = q.popleft()
        if cnt > 10:
            return -1

        if check(coin1_x, coin1_y) * check(coin2_x, coin2_y) == -2:
            return cnt

        for i in range(4):
            coin1_nx = coin1_x + dx[i]
            coin1_ny = coin1_y + dy[i]
            coin2_nx = coin2_x + dx[i]
            coin2_ny = coin2_y + dy[i]
            if check(coin1_nx, coin1_ny) == -1 and check(coin2_nx, coin2_ny) == -1:
                continue
            if not check(coin1_nx, coin1_ny):
                coin1_nx, coin1_ny = coin1_x, coin1_y
            if not check(coin2_nx, coin2_ny):
                coin2_nx, coin2_ny = coin2_x, coin2_y
            if (coin1_nx, coin1_ny, coin2_nx, coin2_ny) not in visited:
                q.append((coin1_nx, coin1_ny, coin2_nx, coin2_ny, cnt + 1))
                visited.add((coin1_nx, coin1_ny, coin2_nx, coin2_ny))
    return -1


N, M = map(int, input().split())

graph, coins = [], []
visited = set()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(N):
    graph.append(list(input().rstrip()))
    for j in range(M):
        if graph[i][j] == "o":
            coins.append((i, j))


print(bfs())
