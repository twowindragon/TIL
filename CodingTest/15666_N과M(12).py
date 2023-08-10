'''
 - prev를 사용해서 같은 루프 안에서 같은 숫자가 나오는 것을 방지
'''
def dfs(ans):
    if len(ans) == M:
        print(*ans)
        return
    
    prev = 0
    for i in range(N):
        if ans and ans[-1] > seq[i]:
            continue
        
        if prev != seq[i]:
            prev = seq[i]
            dfs(ans + [seq[i]])
        
        
N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))
visit = [False] * N
dfs([])
