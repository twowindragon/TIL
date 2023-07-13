import sys

input = sys.stdin.readline


def binary_search(start, end):
    answer = 0
    while start <= end:
        router_cnt = 1
        mid = (start + end) // 2
        pre_router = router_list[0]
        for i in range(len(router_list)):
            if router_list[i] - pre_router >= mid:
                router_cnt += 1
                pre_router = router_list[i]
        if router_cnt < C:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer


N, C = map(int, input().split())
router_list = sorted([int(input()) for _ in range(N)])
print(binary_search(1, router_list[-1] - router_list[0]))
