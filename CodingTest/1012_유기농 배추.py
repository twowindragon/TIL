import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


T = int(sys.stdin.readline())
for _ in range(T):
    answer = 0
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for x in range(N):
        for y in range(M):
            if not visited[x][y]:
                if dfs(x, y):
                    answer += 1
    print(answer)
