import sys


input = sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))
dp = seq.copy()
for i in range(1, N):
    dp[i] = max(seq[i], dp[i - 1] + seq[i])
    
print(max(dp))