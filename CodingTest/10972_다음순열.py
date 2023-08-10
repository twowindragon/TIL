# 1 2 4 3 -> 1 3 2 4
# 1 3 4 2 -> 1 4 2 3
# 1 4 2 3 -> 1 4 3 2
# 1 4 3 2 -> 2 1 3 4
'''
 -  뒤에서 부터 뒷 값이 앞 값보다 큰 경우 찾음
 -  찾은 앞 뒤 값의 인덱스를 x,y 라고 할 때, 뒤에서부터 x보다 큰 값이 있는 지 탐색 후 교환
 -  y부터 끝까지 오름차순 정렬
'''
N = int(input())
seq = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if seq[i - 1] < seq[i]:
        for j in range(N-1, i - 1, -1):
            if seq[i - 1] < seq[j]:
                seq[i - 1], seq[j] = seq[j], seq[i - 1]
                seq[i:] = sorted(seq[i:])
                print(*seq)
                exit()
                
print(-1)