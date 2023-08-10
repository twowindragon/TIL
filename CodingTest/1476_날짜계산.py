# 1 1 1   1
# 15 15 15 15
# 1 16 16 16
# 2 17 17 17
# 3 18 18 18
# 5 20 1 20
# 6 21 2 21
# 13 28 9 28
# 14 1 10 29
# 1 2 3
# n % 15 = 1
# n % 28 = 2
# n % 19 = 3
E, S, M = map(int, input().split())
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0
    
for i in range(1, 7981):
    if i % 15 == E and i % 28 == S and i % 19 == M:
        print(i)
        break
