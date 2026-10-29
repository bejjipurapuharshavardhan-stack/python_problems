# Detect Floating Point Number

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/introduction-to-regex/tutorial) tab to know how to to solve.</sub>  

You are given a string $N$.  
Your task is to verify that $N$ is a floating point number.  

In this task, a valid float number must satisfy *all* of the following requirements:  

$\gt$ Number can start with **`+`**, **`-`** or **`.`** symbol.  
$ \ \ \ \ $For example:  
$ \ \ \ \ ✔ \ $+4.50   
$ \ \ \ \ ✔ \ $-1.0   
$ \ \ \ \ ✔ \ $.5   
$ \ \ \ \ ✔ \ $-.7   
$ \ \ \ \ ✔ \ $+.4   
$ \ \ \ \ ✖ $ __`-+4.5`__    

$\gt$ Number must contain *at least* $1$ decimal value.  
$ \ \ \ \ $For example:  
$ \ \ \ \ ✖ $ __`12.`__  
$ \ \ \ \ ✔ \ $12.0     

$\gt$ Number must have exactly one __`.`__ symbol.  
$\gt$ Number must not give any exceptions when converted using $float(N)$.

**Input Format**

The first line contains an integer $T$, the number of test cases.  
The next $T$ line(s) contains a string $N$.




**Constraints**

+ $ 0 < T < 10$

**Output Format**

Output *True* or *False* for each test case.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T19:00:39.102Z  

```py
import re

for _ in range(int(input())):
    try:
        val = input()
        print(bool(re.match(r"^[\+\-]?\d*\.\d+$", val)) and not (val.count('.') > 1))
    except ValueError:
        print(False)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/introduction-to-regex/problem)