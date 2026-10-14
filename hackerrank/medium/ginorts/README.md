# ginortS

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string $S$.   
$S$ contains alphanumeric characters only.  
![](http://i.imgur.com/u7WkSk7.gif)
Your task is to sort the string $S$ in the following manner:

- All sorted *lowercase letters* are ahead of *uppercase letters*. 
- All sorted *uppercase letters* are ahead of digits.
- All sorted *odd digits* are ahead of sorted *even digits*.



**Input Format**

A single line of input contains the string $S$.



**Constraints**

+ $0 < len(S) < 1000$

**Output Format**

Output the sorted string $S$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T15:56:37.177Z  

```py
s = input()

def custom_sort(c):
    if c.islower():
        return (0, c)
    elif c.isupper():
        return (1, c)
    elif c.isdigit():
        if int(c) % 2 != 0: 
            return (2, c)
        else:               
            return (3, c)

sorted_string = "".join(sorted(s, key=custom_sort))

print(sorted_string)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/ginorts/problem)