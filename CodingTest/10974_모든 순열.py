from itertools import permutations
N = int(input())
for p in permutations([i for i in range(1, N+1)], N):
    print(*p)