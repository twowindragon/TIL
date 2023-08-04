import math
N = int(input())
facto = str(math.factorial(N))
answer = 0
for i in range(len(facto)-1, -1, -1):
    if facto[i] != '0':
        break
    answer += 1

print(answer)