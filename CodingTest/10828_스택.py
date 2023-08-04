n = int(input())
command = []
s = []
for _ in range(n):
    a = list(map(str, input().split()))
    command.append(a)

for i in command:
    if i[0] == "push":
        s.append(int(i[1]))
    elif i[0] == "pop":
        if len(s) == 0:
            print(-1)
        else:
            print(s[len(s) - 1])
            s.pop()
    elif i[0] == "size":
        print(len(s))
    elif i[0] == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(s) == 0:
            print(-1)
        else:
            print(s[len(s) - 1])
