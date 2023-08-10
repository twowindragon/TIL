'''
행은 합을 뜻하고 열은 끝자리 수를 뜻함 
'''
T = int(input())
N = 100000
dp = [[0] * 4 for _ in range(N + 1)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, N + 1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) %  1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) %  1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) %  1000000009
    
# dp = [0, 1, 1, 3, 3, 4, 7, 9]
for _ in range(T):
    n = int(input())
    print(sum(dp[n])%  1000000009)
    