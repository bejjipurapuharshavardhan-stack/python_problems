import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = list(itertools.product(A, B))

# to print space-separated tuples instead of a list:
print(*res)
