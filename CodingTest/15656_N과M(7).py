def product(ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        product(ans + [seq[i]])
        
        
N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

product([])
