import sys


def dfs(team1):
    global ans
    if len(team1) == N // 2:
        team1_stat, team2_stat = 0, 0
        team2 = []
        for i in range(N):
            if i not in team1:
                team2.append(i)
        for i in range(N//2):
            for j in range(i + 1, N//2):
                team1_stat += stats[team1[i]][team1[j]]
                team1_stat += stats[team1[j]][team1[i]]
                team2_stat += stats[team2[i]][team2[j]]
                team2_stat += stats[team2[j]][team2[i]]
        ans = min(ans, abs(team1_stat - team2_stat))
        return
    
    for i in range(N):
        if team1 and team1[-1] <= i:
            continue
        dfs(team1 + [i])
        


N = int(sys.stdin.readline())
stats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = int(1e9)
dfs([])
print(ans)




# def dfs(idx, n):
#     global ans
#     if n == N // 2:
#         team1_stat, team2_stat = 0, 0
#         for i in range(N):
#             for j in range(N):
#                 if visited[i] and visited[j]:
#                     team1_stat += stats[i][j]
#                 elif not visited[i] and not visited[j]:
#                     team2_stat += stats[i][j]
                    
#         ans = min(ans, abs(team1_stat - team2_stat))
#         return
    
#     for i in range(idx, N):
#         if not visited[i]:
#             visited[i] = True
#             dfs(i + 1, n + 1)
#             visited[i] = False


# N = int(sys.stdin.readline())
# stats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# visited = [False] * N
# ans = int(1e9)
# dfs(0, 0)
# print(ans)