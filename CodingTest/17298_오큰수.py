'''
하나씩 인덱스를 스택에 집어 넣다가 집어 넣으려는 값이 스택의 마지막 값보다 큰 경우
계속 스택에서 꺼내주면서 기록한다
'''
import sys
N = int(input())
seq = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [-1] * N
for i in range(N):

    while stack and seq[stack[-1]] < seq[i]:
        answer[stack.pop()] = seq[i]
    
    stack.append(i)
print(*answer)