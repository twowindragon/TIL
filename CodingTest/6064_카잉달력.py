import sys
T = int(input())

def find_K(M, N, x, y):
    K = x

    while K <= M * N:
        if (K - x) % M == 0 and (K - y) % N == 0:
            return K
        K += M
    return -1

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())
    print(find_K(M, N, x, y))