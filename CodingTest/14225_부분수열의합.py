from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))
combs = set()
# for i in range(1, N + 1):
#     for c in combinations(seq, i):
#         combs.add(sum(c))
answer = 1
# while True:
#     if answer not in combs:
#         print(answer)
#         break
#     answer += 1
      
def dfs(idx, num):
    if num:
        combs.add(num)
    if idx >= N:
        return
    dfs(idx + 1, num + seq[idx])
    dfs(idx + 1, num)

dfs(0, 0)
while True:
    if answer not in combs:
        print(answer)
        break
    answer += 1
print(combs)