from collections import deque

for _ in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    
    last_block = float('inf')
    possible = True
    
    while blocks:
        if blocks[0] > blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()
            
        if current > last_block:
            possible = False
            break
            
        last_block = current
        
    if possible:
        print("Yes")
    else:
        print("No")
