a, b = map(int, input().split())


def gcd(a, b):
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b 
    return b

print(gcd(a, b))
print(a * b // gcd(a, b) )