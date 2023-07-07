import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == 100:
            return visited[100]

        for dx in range(1, 7):
            nx = x + dx
            if nx > 100:
                continue

            if nx in pos2pos:
                nx = pos2pos[nx]

            if not visited[nx]:
                queue.append(nx)
                visited[nx] = visited[x] + 1


N, M = map(int, sys.stdin.readline().split())
visited = [0] * 101
pos2pos = {}
for _ in range(N + M):
    i, j = map(int, sys.stdin.readline().split())
    pos2pos[i] = j


print(bfs(1))
