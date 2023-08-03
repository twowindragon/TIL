# 파란구슬이 빠지면 실패, 빨간 구슬과 동시에 빠져도 실패
# 빨, 파 구슬 동시에 같은 칸 불가.
#  '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는  벽, 'O'는 구멍의 위치
# 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1

# 1. 아이디어
''' bfs 알고리즘을 써보자. 
    빨간공을 움직이고, 파란공을 움직인다
    움직일때 다음 칸이 벽이 아니면 움직이고, 들어간 곳이 구멍이면, 파란구슬 일직선 상에 있는 지 확인
'''
# 2. 시간복잡도
''' 4^10 -> 4 * 2^9 ?
            '''

# 3. 자료구조
''' 
    set visit
    bfs의 큐
    그래프 행렬  
    빨, 파란 공 위치 변수 '''
    
from collections import deque



def move(nx, ny, i):
    
    while graph[nx + dx[i]][ny + dy[i]] != '#' and  graph[nx + dx[i]][ny + dy[i]] != 'O': 
        nx += dx[i]
        ny += dy[i]
        
    return nx, ny


def bfs(x, y, b_x, b_y):
        visited = set()
        q = deque([(x, y, b_x, b_y, 0)])
        visited.add((x, y, b_x, b_y))
        while q:
            x, y, b_x, b_y, cnt = q.popleft()

            if cnt >= 10:
                return -1 
            
            for i in range(4):
                nx, ny = move(x, y, i)
                b_nx, b_ny = move(b_x, b_y, i)
                
                if graph[b_nx + dx[i]][b_ny + dy[i]] == 'O':
                        continue
                     
                if graph[nx + dx[i]][ny + dy[i]] == 'O':
                    return cnt + 1
                
                # 0: 북 1: 서 2:남 3:동
                if nx == b_nx and ny == b_ny:
                    if i == 0:
                        if x < b_x:
                            b_nx += 1
                        else:
                            nx += 1
                    elif i == 2:
                        if x > b_x:
                            b_nx -= 1
                        else:
                            nx -= 1
                    elif i == 1:
                        if y < b_y:
                            b_ny += 1
                        else:
                            ny += 1
                    else:
                        if y > b_y:
                            b_ny -= 1
                        else:
                            ny -= 1  
                
                
                if (nx, ny, b_nx, b_ny) not in visited:
                    visited.add((nx, ny, b_nx, b_ny))
                    q.append((nx, ny, b_nx, b_ny,  cnt + 1))
        return -1     
              
N, M = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
graph = []
for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] == 'R':
            red_x, red_y = i, j
        elif graph[i][j] == 'B':
            blue_x, blue_y = i, j   

print(bfs(red_x, red_y, blue_x, blue_y))