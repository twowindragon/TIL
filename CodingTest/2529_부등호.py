'''
 - 0 부터 순서대로 탐색하니 처음 발견하는 것이 최소값
'''

# 연산자 계산
def possible(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j
    
    return True


def dfs(n, num):
    global min_ans, max_ans
    if n == K + 1:
        if not len(min_ans):
            min_ans = num
        else:
            max_ans = num
        return 
    
    for i in range(10):
        if not visited[i]: 
            if n == 0 or possible(num[-1], str(i), inequality[n - 1]):
                visited[i] = True
                dfs(n + 1, num + str(i))
                visited[i] = False
            
K = int(input())
inequality = list(input().split())
visited = [False] * 10
min_ans, max_ans = '', ''

dfs(0, '')
print(max_ans, min_ans, sep='\n')
  