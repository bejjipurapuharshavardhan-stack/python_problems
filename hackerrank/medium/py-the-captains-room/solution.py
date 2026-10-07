from collections import Counter

K = int(input())
my_list = list(map(int, input().split()))

# This counts all numbers in just 1 single pass!
counts = Counter(my_list)

for i in counts:
    if counts[i] == 1:  
        print(i)
        break           


