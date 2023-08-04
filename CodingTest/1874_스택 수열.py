# 수열의 값보다 작으면 쭉 넣고, 그 다음 pop한 값이 수열의 값과 다르면 NO

from sys import stdin
N = int(input())
seq = map(lambda x : int(x.rstrip()), stdin.readlines())


def solution():
    stack = []
    answer = []
    j = 1      
    for i in seq:
        while j <= i:
            stack.append(j)
            j += 1
            answer.append('+')
        if stack.pop() != i:
            return 'NO'
        answer.append('-')
    return '\n'.join(answer)

print(solution())