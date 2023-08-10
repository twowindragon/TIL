def combinations(x, ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(x + 1, N + 1):
        combinations(i, ans + [i])
        
        
N, M = map(int, input().split())

combinations(0, [])
