# Incorrect Regex

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string $S$.  
Your task is to find out whether $S$ is a valid [regex](https://en.wikipedia.org/wiki/Regular_expression) or not.

**Input Format**

The first line contains integer $T$, the number of test cases.  
The next $T$ lines contains the string $S$.

__Constraints__

$0 < T < 100$

**Output Format**

Print "True" or "False" for each test case without quotes.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T17:04:44.644Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

test_cases = int(raw_input())

for _ in range(test_cases):
    pattern = raw_input()
    try:
        re.compile(pattern)
        print True
    except re.error:
        print False

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/incorrect-regex/problem)