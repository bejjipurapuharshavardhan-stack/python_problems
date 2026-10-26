# Piling Up!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is a horizontal row of $n$ cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if $cube[i]$ is on top of $cube[j]$ then $sideLength[j]\ge sideLength[i]$. 

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print `Yes` if it is possible to stack the cubes. Otherwise, print `No`.  

**Example**   
$blocks = [1, 2, 3, 8, 7]$   

Result: `No`  

After choosing the rightmost element, $7$, choose the leftmost element, $1$.  After than, the choices are $2$ and $8$.  These are both larger than the top block of size $1$.

$blocks = [1, 2, 3, 7, 8]$   

Result: `Yes`

Choose blocks from right to left in order to successfully stack the blocks.   

**Input Format**

The first line contains a single integer $T$, the number of test cases.  
For each test case, there are $2$ lines.  
The first line of each test case contains $n$, the number of cubes.  
The second line contains $n$ space separated integers, denoting the *sideLengths* of each cube in that order.  



**Constraints**

$1\le T \le 5$  
$1\le n\le 10^5$  
$1\le sideLength < 2^{31}$

**Output Format**

For each test case, output a single line containing either `Yes` or `No`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T14:13:15.440Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/piling-up/problem)