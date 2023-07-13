import sys
input = sys.stdin.readline


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in range(1, N+1):
            total += min(mid//i, N) #mid 이하의 i의 배수 or 최대 N
        if total >= k: 
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


N = int(input())
k = int(input())
print(binary_search(1, k))