import sys


def binary_search(start, end):
    answer = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for lan in lan_list:
            total += lan // mid
        if total < N:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer


input = sys.stdin.readline
K, N = map(int, input().split())
lan_list = sorted([int(input()) for _ in range(K)])
print(binary_search(1, lan_list[-1]))
