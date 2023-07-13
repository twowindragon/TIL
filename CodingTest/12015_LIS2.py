import sys
input = sys.stdin.readline


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
            
    return start
            
N = int(input())
sequence = list(map(int, input().split()))
lis = [0]

for s in sequence:
    if lis[-1] < s:
        lis.append(s)
    else:
        idx = binary_search(s, 1, len(lis))
        lis[idx] = s

print(len(lis) - 1)