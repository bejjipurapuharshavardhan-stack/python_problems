K = int(input())
my_list = list(map(int, input().split()))

my_list.sort()
n = len(my_list)

i = 0
while i < n:
    j = i
    while j < n and my_list[j] == my_list[i]:
        j += 1
    if j - i != K:
        print(my_list[i])
        break
    i = j










      


