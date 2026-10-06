from itertools import combinations

S, k = input().split()

for i in range(1, int(k) + 1):
    # Generate combinations of size i using the sorted string
    for c in combinations(sorted(S), i):
        print("".join(c))
