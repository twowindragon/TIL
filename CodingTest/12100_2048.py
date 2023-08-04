''' 
# 아이디어
 dfs 써서 최대값 찾기
 블록 이동에 신경쓰기(합쳐지는 순서)

# 시간복잡도
 4방향 ^ 5 * N*N(블록 이동) = 400 * 16 * 64 -> 가능
''' 
# d = 0 : 위 1: 아래 2: 왼쪽 3: 오른쪽


### 내가 구현한 건 3중 반복문... -> 포인터를 사용하면 이중으로 바꿀 수 있다.



# def move_block(d, board):

#     if d == 0:
#         for y in range(N):
#             for x in range(N):
#                 if board[x][y] != 0:
#                     for k in range(x + 1, N):
#                         if board[k][y] != 0:
#                             if board[x][y] != board[k][y]:
#                                 break
#                             board[x][y] *= 2
#                             board[k][y] = 0
#                             break
#             for x in range(N):
#                 if board[x][y] == 0:
#                     for k in range(x + 1, N):
#                         if board[k][y] != 0:
#                             board[x][y], board[k][y] = board[k][y], board[x][y]
#                             break
#     elif d == 1:
#         for y in range(N):
#             temp = []
#             for x in range(N-1, -1, -1):
#                 if board[x][y] != 0:
#                     for k in range(x-1, -1, -1):
#                         if board[k][y] != 0:
#                             if board[x][y] != board[k][y]:
#                                 break
#                             board[x][y] *= 2
#                             board[k][y] = 0
#                             break
#             for x in range(N-1, -1, -1):
#                 if board[x][y] == 0:
#                     for k in range(x-1, -1, -1):
#                         if board[k][y] != 0:
#                             board[x][y], board[k][y] = board[k][y], board[x][y]
#                             break

#     elif d == 2:
#         for x in range(N):
#             temp = []
#             for y in range(N):
#                 if board[x][y] != 0:
#                     for k in range(y+1, N):
#                         if board[x][k] != 0:
#                             if board[x][y] != board[x][k]:
#                                 break
#                             board[x][y] *= 2
#                             board[x][k] = 0
#                             break
#             for y in range(N):
#                 if board[x][y] == 0:
#                     for k in range(y+1, N):
#                         if board[x][k] != 0:
#                             board[x][y], board[x][k] = board[x][k], board[x][y]
#                             break                                                
                            
#     elif d == 3:
#         for x in range(N):
#             temp = []
#             for y in range(N-1, -1, -1):
#                 if board[x][y] != 0:
#                     for k in range(y - 1, -1, -1):
#                         if board[x][k] != 0:
#                             if board[x][y] != board[x][k]:
#                                 break
#                             board[x][y] *= 2
#                             board[x][k] = 0
#                             break
                        
#             for y in range(N-1, -1, -1):
#                 if board[x][y] == 0:
#                     for k in range(y - 1, -1, -1):
#                         if board[x][k] != 0:
#                             board[x][y], board[x][k] = board[x][k], board[x][y]
#                             break                       
#     return board            


import copy
# 수정 코드
'''
현재 포인터가 가리키는 값이 0 이면 탐색한 값을 포인터에 넣고, 탐색 위치에는 0 저장 
현재 포인터가 가리키는 값과 탐색한 값이 동일하면 포인터값 *2 를 하고, 포인터를 하나 증가시킴
현재 포인터가 가리키는 값과 탐색 값이 다르면 포인터 증가시키고 대입
포인터 위치와 탐색위치 사이에는 0 이 존재하거나 아니면 위치가 하나차이날 수 밖에 없음
즉 그 사이에는 0이 아닌 값이 없을 것임 차례대로 탐색 위치의 값을 다 처리 해줬기 때문에
'''
def move_block(d, board):
    # d = 0 : 위 1: 아래 2: 왼쪽 3: 오른쪽
    if d == 0:
        for j in range(N):
            pointer = 0
            for i in range(1, N):
                if board[i][j] != 0: # 탐색 위치 -> 0이 아닌 값
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0: # 포인터를 증가시키지 않은 이유는 다음 탐색값과 동일한 값일 수도..
                        board[pointer][j] = temp

                    elif board[pointer][j] == temp:
                        board[pointer][j] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[pointer][j] = temp
    
    elif d == 1:
        for j in range(N):
            pointer = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = temp
                    elif board[pointer][j]  == temp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = temp
    
    elif d == 2:
        for i in range(N):
            pointer = 0
            for j in range(1, N):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = temp
                    elif board[i][pointer]  == temp:
                        board[i][pointer] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer]= temp
    else:
        for i in range(N):
            pointer = N - 1
            for j in range(N - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = temp
                    elif board[i][pointer]  == temp:
                        board[i][pointer] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = temp
            
    return board

def dfs(x, board):
    global answer
    if x == 5:
        # max값 찾기
        answer = max(answer, max(map(max, board)))
        return
    
    for i in range(4):
        graph = copy.deepcopy(board)
        dfs(x + 1, move_block(i, graph))
        
        
answer = 0
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dfs(0, board)
print(answer)