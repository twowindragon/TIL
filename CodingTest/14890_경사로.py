"""
 - 4방향 모두 탐색
 - 작아지면 L 만큼 같은 지 이동 
 
"""

import sys

input = sys.stdin.readline
N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0


for i in range(N):
    pointer = 0
    cnt = 0
    down = False
    for j in range(N):
        if down:
            if cnt >= L:
                pointer = j - 1
                cnt = 0
                down = False

        if graph[i][pointer] == graph[i][j]:
            cnt += 1
        else:
            if down:
                break

            if graph[i][pointer] == graph[i][j] - 1:
                if cnt >= L:
                    pointer = j
                    cnt = 1
                else:
                    break

            elif graph[i][pointer] == graph[i][j] + 1:
                down = True
                pointer = j
                cnt = 1
            else:
                break
    else:
        if down and cnt < L:
            continue
        ans += 1

for j in range(N):
    pointer = 0
    cnt = 0
    down = False
    for i in range(N):
        if down:
            if cnt >= L:
                pointer = i - 1
                cnt = 0
                down = False

        if graph[pointer][j] == graph[i][j]:
            cnt += 1
        else:
            if down:
                break

            if graph[pointer][j] == graph[i][j] - 1:
                if cnt >= L:
                    pointer = i
                    cnt = 1
                else:
                    break
            elif graph[pointer][j] == graph[i][j] + 1:
                down = True
                pointer = i
                cnt = 1
            else:
                break

    else:
        if down and cnt < L:
            continue
        ans += 1

print(ans)
