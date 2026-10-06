from itertools import permutations

S, k = input().split()

# Generate the permutations and print them
for p in permutations(sorted(S), int(k)):
    print("".join(p))
