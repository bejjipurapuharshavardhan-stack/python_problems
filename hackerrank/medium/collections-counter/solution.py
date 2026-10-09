from collections import Counter

shoes_num = int(input())
my_list = list(map(int, input().split()))
customers = int(input())

total_revenue = 0
# Change the square brackets to parentheses here:
inventory = Counter(my_list)

for _ in range(customers):
    size, prize = map(int, input().split())
    if inventory[size] > 0:
        total_revenue += prize
        inventory[size] -= 1

print(total_revenue)
