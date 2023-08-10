def product(ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(1, N + 1):
        product(ans + [i])
        
        
N, M = map(int, input().split())

product([])
