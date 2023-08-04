def check_vps(ps):
    stack = []
    for bracket in PS:
        if bracket == ")":
            if not stack:
                return False
            stack.pop()
            continue
        elif bracket == "(":
            stack.append(bracket)
    if stack:
        return False
    return True


T = int(input())
for _ in range(T):
    PS = list(input())
    if check_vps(PS):
        print("YES")
    else:
        print("NO")
