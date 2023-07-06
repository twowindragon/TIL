import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs(start, end):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == end:
            return visited[x]
        for nx in [x + 1, x - 1, 2 * x]:
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)


N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
print(bfs(N, K))
