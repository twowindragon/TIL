'''
')' 일때 그전의 문자가 '('면 레이저 -> 스택의 수만큼 플러스
          ')'일 때는  쇠막대기 -> 1만 더해줌

'''
laser = list(input())
stack = []
answer = 0
for i in range(len(laser)):
    if laser[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if laser[i-1] == '(':       
            answer += len(stack)
        else:
            answer += 1
print(answer)
