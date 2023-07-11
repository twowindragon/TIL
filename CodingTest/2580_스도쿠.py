import sys

def check_row(c, i):
    for x in range(9):
        if graph[x][c] == i:
            return False
    return True
    

def check_col(r, i):
    for y in graph[r]:
        if i == y:
            return False
    return True

def check_rect(r, c, i):
    for x in range(r // 3 * 3, r // 3 * 3 + 3):
        for y in range(c // 3 * 3, c // 3 * 3 + 3):
            if graph[x][y] == i:
                return False
            
    return True


def sudoku(n):
    if n == len(zeros):
        for g in graph:
            print(*g)
        exit()
        
    x, y = zeros[n]
    for i in range(1, 10):
        if check_row(y, i) and check_col(x, i) and check_rect(x, y, i):
            graph[x][y] = i
            sudoku(n+1)
            graph[x][y] = 0
        
    

zeros = []
graph = []
for x in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for y in range(9):
        if graph[x][y] == 0:
            zeros.append((x, y))

sudoku(0)