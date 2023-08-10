def permutations(ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        if seq[i] not in ans:
            permutations(ans + [seq[i]])
        
        
N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

permutations([])
