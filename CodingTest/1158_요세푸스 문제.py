from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])
answer = []
while q:
    cnt = len(q) % K
    for _ in range(K - 1):
        q.append(q.popleft())
    answer.append(q.popleft())  
print('<', end='')
print(*answer, sep=', ', end='')
print('>')
