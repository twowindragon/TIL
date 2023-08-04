N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = len(A)
for people in A:
    people -= B
    if people > 0:
        answer += (people - 1) // C + 1 

print(answer)