import math

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a * b // math.gcd(a, b))