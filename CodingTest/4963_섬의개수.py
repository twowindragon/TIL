import sys
sys.setrecursionlimit(10**9)

def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True  
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)
        return True    
    return False


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        exit()
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                answer += 1
    print(answer)