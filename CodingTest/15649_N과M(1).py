def combinations(ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(1, N + 1):
        if i in ans:
            continue
        combinations(ans + [i])
        
        
N, M = map(int, input().split())

combinations([])
