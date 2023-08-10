def solution(N, M, break_buttons):
    temp = 1e9
    temp2 = 1e9
    answer = 0
    for i in range(1e6 + 1):
        minus = N - i
        plus = N + i
        if minus > - 1:
            for num in str(minus):
                if int(num) in break_buttons:
                    break
            else:
                temp = minus
                break
     
        for num in str(plus):
            if int(num) in break_buttons:
                break
        else:
            temp2 = plus
            break
    
    return min(len(str(temp)) + i, abs(N - 100), len(str(temp2)) + i) 
    
N = int(input())
M = int(input())
if M:
    break_buttons = list(map(int, input().split()))
else:
    break_buttons = []
    
print(solution(N, M, break_buttons))