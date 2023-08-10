def diff(ans):
    temp = 0
    for i in range(N - 1):
        temp += abs(ans[i] - ans[i + 1])    
    return temp

def dfs(ans):
    global answer
    if len(ans) == N:
        answer = max(diff(ans), answer)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(ans + [seq[i]])
            visited[i] = False


N = int(input())
seq = list(map(int, input().split()))
visited = [False] * N
answer = 0
dfs([])
print(answer)