def dfs(ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        if ans and ans[-1] > seq[i]:
            continue
        
        dfs(ans + [seq[i]])
        
        
N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

dfs([])
