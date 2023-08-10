N = int(input())
dp = [i for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j **2] + 1)

print(dp[N])
# 1: 1
# 2: 2
# 3: 3
# 4: 1
# 5: 2
# 6: 3
# 7: 4
# 8: 2
# 9: 1
# 10: 2
# 11: 3
# 13: 2 -> 4 + 9
# 35: 3
# 77: 8 3 2
# 98 7 7