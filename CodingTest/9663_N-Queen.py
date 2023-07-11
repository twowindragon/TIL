def promising(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        elif abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def N_Queen(x):
    global answer
    if x == len(row):
        answer += 1
        return

    for i in range(N):
        row[x] = i
        if promising(x):
            N_Queen(x + 1)


answer = 0
N = int(input())
row = [0] * N
N_Queen(0)
print(answer)
