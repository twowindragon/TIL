import sys
from collections import Counter
input = sys.stdin.readline
r, g, k = map(int, input().split())
r, g = r - 1, g - 1
graph = [list(map(int, input().split())) for _ in range(3)]

ans = 0

while True:
    len_r = 1
    len_c = 1
    if len(graph) > r and len(graph[0]) > g and graph[r][g] == k:
        break
    if ans > 100:
        ans = -1
        break

    if len(graph) >= len(graph[0]):

        for i in range(len(graph)):
            c = Counter(graph[i])
            if 0 in c:
                del c[0]
            c = sorted(c.items(), key=lambda x: (x[1], x[0]))
            d = []
            for b in c:
                d.extend([*b])
            len_c = max(len(d), len_c)
            graph[i] = d
        for i in range(len(graph)):
            if len(graph[i]) < len_c:
                graph[i].extend([0] * (len_c - len(graph[i])))
        # print('행정렬')
        # for i in graph:
        #     print(i)
    else:
        f = len(graph)
        for i in range(len(graph[0])):
            c = []
            for j in range(f):
                if graph[j][i] == 0:
                    continue
                c.append(graph[j][i])

            c = sorted(Counter(c).items(), key=lambda x: (x[1], x[0]))
            d = []
            for b in c:
                d.extend([*b])

            len_r = max(len(d), len_r)
            if len(graph) < len_r:
                graph.extend([[0] * len(graph[0])
                             for _ in range(len_r - len(graph))])
            for j in range(len(graph)):
                if j < len(d):
                    graph[j][i] = d[j]
                else:
                    graph[j][i] = 0

        # print('열 정렬')
        # for i in graph:
        #     print(i)
        # print()
    ans += 1
print(ans)
