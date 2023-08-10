def insert_op(idx, ans):
    global max_ans, min_ans, add, sub, mul, div
    if idx == N - 1:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return

    if add:
        add -= 1
        insert_op(idx + 1, ans + nums[idx + 1])
        add += 1
    if sub:
        sub -= 1
        insert_op(idx + 1, ans - nums[idx + 1])
        sub += 1
    if mul:
        mul -= 1
        insert_op(idx + 1, ans * nums[idx + 1])
        mul += 1
    if div:
        div -= 1
        insert_op(idx + 1, int(ans / nums[idx + 1]))
        div += 1


N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_ans = int(1e9)
max_ans = int(-1e9)
insert_op(0, nums[0])
print(max_ans, min_ans, sep="\n")
