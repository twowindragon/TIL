from collections import deque


def path(x):
    arr = []
    temp = x
    for _ in range(vistied[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(*arr[::-1])
    
def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == K:
            print(vistied[x])
            path(x)
            return 
        for nx in [x + 1, x - 1, x * 2]:
            if nx < 0 or nx >= 100001:
                continue
            if vistied[nx] == 0:
                vistied[nx] = vistied[x] + 1
                q.append(nx)
                move[nx] = x
                
        

N, K = map(int, input().split())
vistied = [0] * 100001
move = [0] * 100001
bfs(N)

