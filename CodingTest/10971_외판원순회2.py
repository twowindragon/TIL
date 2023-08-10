from itertools import permutations
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
for p in permutations([i for i in range(N)], N):
    path = list(p)
    path.append(path[0])
    temp = 0
    for i in range(len(path)-1):
        if graph[path[i]][path[i + 1]] == 0:
            break
        temp += graph[path[i]][path[i + 1]]
        if temp > answer:
            break
    else:
        answer = min(answer, temp)
        
print(answer)