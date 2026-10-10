from collections import OrderedDict

n = int(input())

sales = OrderedDict()

for _ in range(n):
    data = input().split()
    
    price = int(data[-1])
    
    item_name = " ".join(data[:-1])
    
    if item_name in sales:
        sales[item_name] += price
    else:
        sales[item_name] = price

for item, net_price in sales.items():
    print(f"{item} {net_price}")
