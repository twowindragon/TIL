from itertools import combinations
a = []
for _ in range(9):
  a.append(int(input()))
cbs = combinations(a, 7)
for c in cbs:
  if sum(c) == 100:
    answer = sorted(list(c))

print(*answer, sep='\n')