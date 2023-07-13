import sys
import bisect
from collections import Counter


def binary_search(arr, target, start, end):
    left_index = bisect.bisect_left(arr, target)
    right_index = bisect.bisect_right(arr, target)
    return right_index - left_index


N = int(input())
# target_list = sorted(list(map(int, sys.stdin.readline().split())))
target_list = list(map(int, sys.stdin.readline().split()))
M = int(input())
find_list = list(map(int, sys.stdin.readline().split()))
end = len(target_list) - 1
# for i in find_list:
#     print(binary_search(target_list, i, 0, end))
count = Counter(target_list)
for i in find_list:
    if i in count:
        print(count[i])
    else:
        print(0)
