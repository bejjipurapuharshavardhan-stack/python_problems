from itertools import combinations

list_size = int(input())
my_list = input().lower().split()
K = int(input())

total = 0
good = 0
for combo in combinations(my_list, K):
    total += 1
    if 'a' in combo:
        good += 1

print(round(good / total, 4))




