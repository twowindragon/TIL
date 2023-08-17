import sys

def dfs(idx, num):
    global answer
    if num == S and idx:
        answer += 1
        # print(idx)
    for i in range(idx, N):
        dfs(i + 1, num + seq[i])
        
input = sys.stdin.readline
N, S = map(int, input().split())
seq = list(map(int, input().split()))
answer = 0
dfs(0, 0)
print(answer)
##############
# def dfs(num,sum):
# 	global cnt
# 	if num >= n:
# 		return
# 	sum += n_list[num]
# 	if sum == s:
# 		cnt += 1


# 	dfs(num+1,sum)
# 	dfs(num+1,sum-n_list[num])

# dfs(0,0)
# print(cnt)