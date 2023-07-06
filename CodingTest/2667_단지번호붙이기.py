import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[False] * N for _ in range(N)]
answer = []


def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        cnt += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            cnt = 0
            if dfs(x, y):
                answer.append(cnt)

print(len(answer))
print(*sorted(answer), sep='\n')
