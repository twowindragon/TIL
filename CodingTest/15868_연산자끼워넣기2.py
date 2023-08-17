import sys    


def dfs(idx, num):
    global min_answer, max_answer, add, sub, mul, div
    if idx == N - 1:
        min_answer = min(min_answer, num)
        max_answer = max(max_answer, num)
        return
    
    if add:
        add -= 1
        dfs(idx + 1, num + seq[idx + 1])
        add += 1
    if sub:
        sub -= 1
        dfs(idx + 1, num - seq[idx + 1])
        sub += 1
    if mul:
        mul -= 1
        dfs(idx + 1, num * seq[idx + 1])
        mul += 1
    if div:
        div -= 1
        dfs(idx + 1, int(num / seq[idx + 1]))
        div += 1   
        
N = int(input())
seq = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_answer, max_answer = int(1e9), -int(1e9)
dfs(0, seq[0])
print(max_answer, min_answer, sep='\n')