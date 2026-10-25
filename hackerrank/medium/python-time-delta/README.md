# Time Delta

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago. 

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format: 

`Day dd Mon yyyy hh:mm:ss +xxxx`

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.  






**Input Format**

The first line contains $T$, the number of testcases.  
Each testcase contains $2$ lines, representing time $t_1$ and time $t_2$. 



**Constraints**

+ Input contains only valid timestamps
+ $year ~ \le 3000$. 

**Output Format**

Print the absolute difference $(t_1 - t_2)$ in seconds.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T17:14:51.522Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

def time_delta(t1, t2):
    
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return str(int(abs((datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-time-delta/problem)