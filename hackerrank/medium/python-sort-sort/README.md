# Athlete Sort

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a spreadsheet that contains a list of $N$ athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the $K$<sup>th</sup> attribute and print the final resulting table. Follow the example given below for better understanding. 

![image](https://s3.amazonaws.com/hr-assets/0/1514874268-6fabad07aa-AthleteSort2.png)

Note that $K$ is indexed from $0$ to $M-1$, where $M$ is the number of attributes. 
 
**Note**: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

**Input Format**

The first line contains $N$ and $M$ separated by a space.      
The next $N$ lines each contain $M$ elements.      
The last line contains $K$.     

**Constraints**

$1 \le N,M \le 1000$  
$0 \le K < M$  
Each element $\le 1000$


**Output Format**

Print the $N$ lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T18:17:36.428Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda row: row[k])
    
    for row in arr:
        print(*row)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-sort-sort/problem)