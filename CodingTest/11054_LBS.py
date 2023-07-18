# import sys

# input = sys.stdin.readline
# N = int(input())
# dp = [[1] * 2 for _ in range(N)]
# lbs = list(map(int, input().split()))
# max_result = 0
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         if lbs[i] < lbs[j]:
#             dp[j][0] = max(dp[j][0], dp[i][0] + 1)

# lbs = lbs[::-1]
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         if lbs[i] < lbs[j]:
#             dp[N - j - 1][1] = max(dp[N - j - 1][1], dp[N - i - 1][1] + 1)

# for i in range(N):
#     max_result = max(max_result, dp[i][1] + dp[i][0])
# print(max_result - 1)

import sys

input = sys.stdin.readline
N = int(input())
dp = [[1] * 2 for _ in range(N)]
lbs = list(map(int, input().split()))
max_result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if lbs[i] < lbs[j]:
            dp[j][0] = max(dp[j][0], dp[i][0] + 1)
        
        if lbs[N - i - 1] < lbs[N - j - 1]:
            dp[N - j - 1][1] = max(dp[N - j - 1][1], dp[N - i - 1][1] + 1)

for i in range(N):
    max_result = max(max_result, dp[i][1] + dp[i][0])
print(max_result - 1)
