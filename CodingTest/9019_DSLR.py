"""
 - 0 이상 10,000 미만
 - D: n * 2 if n * 2 <= 9999 else n * 2 % 10000
 - S: n - 1 if n != 0 else 9999
 - L: int(str(n)[1:] + str(n)[0]) 1234 -> 2341
 - R: int(str(n)[-1] + str(n)[:-1])
"""
from collections import deque


def op(i, n):
    if i == 0:
        return n * 2 if n * 2 < 10000 else n * 2 % 10000, "D"
    elif i == 1:
        return n - 1 if n != 0 else 9999, "S"
    elif i == 2:
        n = str(n).zfill(4)
        return int(n[1:] + n[0]), "L"
    else:
        n = str(n).zfill(4)
        return int(n[-1] + n[:-1]), "R"


def bfs():
    q = deque([(A, "")])
    visited[A] = True
    while q:
        x, command = q.popleft()
        if x == B:
            return command
        for i in range(4):
            nx, next_command = op(i, x)
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, command + next_command))


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    print(bfs())