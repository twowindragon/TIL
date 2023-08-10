def dfs(ans):
    if len(ans) == 6:
        print(*ans)
        return
    for i in range(K):
        if ans and ans[-1] >= S[i]:
            continue
        dfs(ans + [S[i]])
        
while True:
    K, *S = map(int, input().split())
    if K == 0:
        exit()
    dfs([])
    print()