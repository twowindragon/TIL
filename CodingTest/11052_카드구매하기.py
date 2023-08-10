N = int(input())
P = list(map(int, input().split()))
dp = P.copy()
for i in range(2, N + 1):
   for j in range(1, i // 2 + 1):
       dp[i - 1] = max(dp[i - j - 1] + P[j - 1], dp[i - 1])

print(dp[N - 1])
