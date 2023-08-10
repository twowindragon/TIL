'''
 - prev를 사용해서 같은 루프 안에서 같은 숫자가 나오는 것을 방지
'''
def dfs(ans):
    if len(ans) == M:
        print(*ans)
        return
    
    prev = 0
    for i in range(N):
        if not visit[i] and prev != seq[i]:
            visit[i] = True
            prev = seq[i]
            dfs(ans + [seq[i]])
            visit[i] = False
        
N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))
visit = [False] * N
answer = []
dfs([])
