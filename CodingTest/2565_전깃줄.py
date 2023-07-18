import sys

input = sys.stdin.readline
N = int(input())
temp = [0] * 500

for _ in range(N):
    i, j = map(int, input().split())
    temp[i - 1] = j

line = [i for i in temp if i != 0]
dp = [1] * N

for i in range(N - 1):
    for j in range(i + 1, N):
        if line[i] < line[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(N - max(dp))
