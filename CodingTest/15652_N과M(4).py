def product(x, ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(x, N + 1):
        product(i, ans + [i])
        
        
N, M = map(int, input().split())

product(1, [])
