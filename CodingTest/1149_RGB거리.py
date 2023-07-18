import sys


input = sys.stdin.readline
N = int(input())
color_cost = []
for _ in range(N):
    color_cost.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N)]
for i in range(3):
    dp[0][i] = color_cost[0][i]

for i in range(1, N):
    dp[i][0] = min(color_cost[i][0] + dp[i - 1][1], color_cost[i][0] + dp[i - 1][2])
    dp[i][1] = min(color_cost[i][1] + dp[i - 1][0], color_cost[i][1] + dp[i - 1][2])
    dp[i][2] = min(color_cost[i][2] + dp[i - 1][0], color_cost[i][2] + dp[i - 1][1])

print(min(dp[N - 1]))
