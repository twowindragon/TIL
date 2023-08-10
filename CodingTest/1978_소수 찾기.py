N = int(input())
nums = list(map(int, input().split()))
answer = 0 
for num in nums:
    if num == 1:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        answer += 1

print(answer)