import sys


def binary_search(start, end, target, arr):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


N = int(input())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    print(binary_search(0, len(n_list) - 1, i, n_list))
