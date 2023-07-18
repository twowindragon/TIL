import sys


input = sys.stdin.readline
N = int(input())
wine_list = [0] * 10000
dp = [[0] * 2 for _ in range(10000)]
for i in range(N):
    wine_list[i] = int(input())

dp[0][0] = wine_list[0]
dp[1][0] = wine_list[1]
dp[1][1] = wine_list[0] + wine_list[1]
for i in range(2, N):
    dp[i][0] = max(
        dp[i - 2][1] + wine_list[i], dp[i - 1][1], dp[i - 2][0] + wine_list[i]
    )
    dp[i][1] = dp[i - 1][0] + wine_list[i]

print(max(dp[N - 1]))
