'''
오른쪽과 아래로만 교환(색깔이 다를 때) 
행 교환 되면 행을 확인, 열 교환 되면 열 확인
'''
import copy


def check(graph, x, y, d):
    cnt_list = [1]
    cnt = 1
    if d == 0:            
        for j in range(N - 1):
            if graph[x][j] == graph[x][j+1]:
                cnt += 1
            else:
                cnt = 1
            cnt_list.append(cnt)
    else:
        for i in range(N - 1):
            if graph[i][y] == graph[i+1][y]:
                cnt += 1
            else:
                cnt = 1  
            cnt_list.append(cnt)      
    
    return max(cnt_list)


def change(x, y, d):

    temp_graph = copy.deepcopy(graph)
    if d == 0:
        temp_graph[x][y], temp_graph[x + 1][y] = temp_graph[x + 1][y], temp_graph[x][y] 
        
    else:  
        temp_graph[x][y], temp_graph[x][y + 1] = temp_graph[x][y + 1], temp_graph[x][y] 
    
    return temp_graph

N = int(input())
graph = [list(input()) for _ in range(N)]

answer = 0
for x in range(N):
    for y in range(N):
        answer = max(answer, check(graph, x, y, 0), check(graph, x, y, 1))
        if x != N - 1:
            if graph[x][y] != graph[x + 1][y]:  
                temp_graph = change(x, y, 0)
                answer = max(answer, check(temp_graph, x, y, 0), check(temp_graph, x + 1, y, 0), check(temp_graph, x, y, 1))
                
        if y != N - 1:            
            if graph[x][y] != graph[x][y + 1]:
                temp_graph = change(x, y, 1)
                answer = max(answer, check(temp_graph, x, y, 1), check(temp_graph, x, y + 1, 1), check(temp_graph, x, y, 0))
                
        if answer == N:
            print(answer)
            exit()
        
print(answer)