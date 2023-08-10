'''
 -  1 <= N <= 15 -> dfs
 -  조건하에 전부 탐색해서 최대 값을 구하면 될 듯
 -  퇴사 날 넘는 건 미리 빼면 편할듯?
'''
def dfs(idx, benefit):
    global answer 
    answer = max(answer, benefit)
    for i in range(idx, N + 1):
        if i not in exceed:
            dfs(i + T[i], benefit + P[i])
    
    
N = int(input())
T, P = [0], [0]
answer = 0
exceed = []
for i in range(1, N + 1):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    if i + t > N + 1:
        exceed.append(i)
dfs(1, 0)
print(answer)