'''
보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 
뱀의 길이는 1 이다. 
뱀은 처음에 오른쪽을 향한다
1. 머리를 늘려 다음칸으로 이동
2. 벽 과 자기자신의 몸 박으면 게임 끝
3. 이동 칸에 사과가 있으면 그대로 없으면 꼬리칸 삭제
4. 몇 초안에 게임이 끝나는가

# 아이디어 
뱀이 올려져있는 위치들을 큐로 관리
-> 머리 이동하면 appendleft 하고 꼬리 짧아지면 pop 함수 사용
사과 위치는 set을 통해 저장
'''
from collections import deque


def snake_game():
    i = 0
    answer = 0
    q = deque([(0, 0)])
    while True:
        if direction:
            if answer == direction[0][0]:
                if direction[0][1] == 'L':
                    i = (i - 1) % 4
                else:
                    i = (i + 1) % 4
                direction.pop(0)
            
        answer += 1
        x, y = q[0]
        nx, ny = x + dx[i], y + dy[i]
        if (nx, ny) in q or nx < 0 or nx >= N or ny < 0 or ny >= N:
            return answer
        q.appendleft((nx, ny))
        if (nx, ny) in apple_set:
            apple_set.remove((nx, ny))
            continue
        q.pop()
        
        
N = int(input())
K = int(input())
apple_set = set()
for _ in range(K):
    x, y = map(int, input().split())
    apple_set.add((x - 1, y - 1))

L = int(input())
direction = []
for _ in range(L):
    X, C = input().split()
    direction.append((int(X), C))
# 위 -1 ,0      3  2 0 L:0, -1    D: 0, 1
# 아래 1, 0     1  0 2  L:0, 1 D: 0, -1
# 왼쪽  0, -1   2  1 3 L: 1, 0 D: -1, 0
# 오른쪽 0, 1   0  3 1 L: -1, 0 D: 1, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(snake_game())

        