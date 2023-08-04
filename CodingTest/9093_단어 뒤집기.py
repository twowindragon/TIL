T = int(input())
for _ in range(T):
    sentence = list(input().split())
    print(' '.join([word[::-1] for word in sentence]))