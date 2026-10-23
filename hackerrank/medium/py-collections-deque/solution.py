from collections import deque

d = deque()
num_oper = int(input())

for _ in range(num_oper):
    methods = input().lower().split()
    if methods[0] == 'append':
        d.append(methods[1])
    elif methods[0] == 'appendleft':
        d.appendleft(methods[1])
    elif methods[0] == 'pop':
        d.pop()
    elif methods[0] == 'popleft':
        d.popleft()

print(*d)


  
