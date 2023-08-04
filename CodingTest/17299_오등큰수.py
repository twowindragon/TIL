'''
오큰수와 유사 
Counter 써서 원소별 등장 횟수 기록하면 될 듯?

'''
import sys
from collections import Counter
N = int(input())
seq = list(map(int, sys.stdin.readline().split()))
count = Counter(seq)
stack = []
answer = [-1] * N
for i in range(N):
    while stack and count[seq[stack[-1]]] < count[seq[i]]:
        answer[stack.pop()] = seq[i]
    stack.append(i)

print(*answer)