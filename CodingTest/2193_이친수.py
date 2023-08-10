# 행은 n자리 수를 뜻하고, 열 0, 1은 마지막 자리수의 숫자를 나타냄
# -> 0이 마지막에 오려면 앞에 1 0 1이 마지막에 오려면 앞에 0이 와야함

N = int(input())
dp = [[0] * 2 for _ in range(N + 1)]
dp[1][1] = 1
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]

print(sum(dp[N]))