

S = list(input())
stack = []    
answer = ''
i = 0
while i < len(S):
    if S[i] == '<':
        while S[i] != '>':
            i += 1
        i += 1
    elif S[i].isalnum():
        start = i
        while i < len(S) and S[i].isalnum():
            i += 1
        S[start:i] = S[start:i][::-1]
    else:
        i += 1
print(''.join(S))