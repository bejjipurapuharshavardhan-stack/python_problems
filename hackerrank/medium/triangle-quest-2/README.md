# Triangle Quest 2

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a positive integer $N$.  
Your task is to print a palindromic triangle of size $N$.  

For example, a palindromic triangle of size $5$ is:  
```python
1
121
12321
1234321
123454321
```		    
You can't take more than two lines. The first line (a *for*-statement) is already written for you.  
You have to complete the code using exactly one print statement.  

**Note**:   
Using anything related to *strings* will give a score of $0$.  
Using more than one *for*-statement will give a score of $0$.


**Input Format**

A single line of input containing the integer $N$.  



**Constraints**

+ $0 < N < 10$

**Output Format**

Print the palindromic triangle of size $N$ as explained above.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T17:21:27.905Z  

```py
for i in range(1, int(input())+1):
    print(((10**i)//9)**2)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/triangle-quest-2/problem)