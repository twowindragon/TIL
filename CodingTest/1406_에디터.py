# stack 과 queue를 이용해서 커서를 기준으로 좌우 나눔

import sys
from collections import deque
editor_l = list(input())
editor_r = deque()
n = int(input())
commands = []
cur = len(editor_l)
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'P':
        editor_l.append(command[1])
    elif command[0] == 'L':
        if editor_l:
            editor_r.appendleft(editor_l.pop())
    elif command[0] == 'D':
        if editor_r:
            editor_l.append(editor_r.popleft())
            
    elif command[0] == 'B':
        if editor_l:
            editor_l.pop()
           
print(''.join(editor_l + list(editor_r)))
