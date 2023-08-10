# i 번째 타일 만드는 방법은 i - 1 번째 타일에 | 추가, i - 2번째 타일에 - 2개 추가

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007 
print(dp[n])