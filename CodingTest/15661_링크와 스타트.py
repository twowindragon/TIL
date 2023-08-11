'''
 - dfs에서 for문을 안쓰는 방식도 고려해보자.
 - 하나씩 값을 증가시키면서 하는 방법도 있음
'''
import sys

def dfs(idx, team1):
    global answer
    if len(team1) > N // 2:
        return 
    
    if 1 <= len(team1) <= N // 2:
        team2 = []
        team1_stat, team2_stat = 0, 0
        for i in range(N):
            if i not in team1:
                team2.append(i)
        
        for i in range(len(team1) - 1):
            for j in range(i + 1, len(team1)):
                team1_stat += stats[team1[i]][team1[j]] + stats[team1[j]][team1[i]]

        for i in range(len(team2) - 1):
            for j in range(i + 1, len(team2)):
                team2_stat += stats[team2[i]][team2[j]] + stats[team2[j]][team2[i]]
        
        answer = min(answer, abs(team1_stat - team2_stat))
        
    for i in range(idx, N):
        dfs(i + 1, team1 + [i])
        
    
N = int(input())
stats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
answer = int(1e9)

dfs(0, [])
print(answer)


############################
# import sys

# input = sys.stdin.readline

# n = int(input())

# matrix = [list(map(int,input().split())) for _ in range(n)]

# visited1 = [False] * n

# min_value = 100*20

# def recur(target):

#     if target == n:
#         score()
#         return


#     visited1[target] = True
#     recur(target+1)
#     visited1[target] = False
#     recur(target+1)
            
    

# def score():
#     global min_value

#     start = 0
#     link = 0

#     for i in range(n-1):
#         for j in range(i+1,n):
#             if visited1[i] and visited1[j] :
#                 start += matrix[i][j] + matrix[j][i]
#             elif not visited1[i] and not visited1[j]:
#                 link += matrix[i][j] + matrix[j][i]
    
#     diff = abs(start-link)

#     if  min_value > diff:
#         min_value = diff



# recur(0)


# print(min_value)