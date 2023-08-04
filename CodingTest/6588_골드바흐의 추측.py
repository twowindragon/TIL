import sys
input = sys.stdin.readline

n = 1000001
# 소수 아닌 모든 홀수 처리
prime = [True] * n
for i in range(3, int(n ** 0.5) + 1, 2):
    if prime[i]:
        for j in range(i * 2, n, i):
            prime[j] = False
# k가 만들어지는 두 홀수인 소수 검색
while 1:
    k = int(input())
    if not k:
        break
    for i in range(3, k // 2 + 1, 2):
        if prime[i] and prime[k - i]:
            print(f"{k} = {i} + {k - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")