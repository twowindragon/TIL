import sys
import heapq
input = sys.stdin.readline

def max_heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
    

def min_heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result    


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

res = min_heapsort(arr)
print(res)
res = max_heapsort(arr)
print(res)