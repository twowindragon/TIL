N = int(input()) + 1
answer = 0
k = len(str(N)) - 1
while k > -1:
    answer += (N - 10 ** k) * (k + 1)
    N = 10 ** k
    k -= 1
   
print(answer)

