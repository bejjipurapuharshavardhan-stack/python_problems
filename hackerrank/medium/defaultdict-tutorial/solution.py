
from collections import defaultdict

n, m = map(int, input().split())
group_A = [input().strip() for _ in range(n)]
group_B = [input().strip() for _ in range(m)]

d = defaultdict(list)
for i in range(n):
    d[group_A[i]].append(str(i + 1))
for word in group_B:
    if word in d:
        print(" ".join(d[word]))
    else:
        print("-1")
