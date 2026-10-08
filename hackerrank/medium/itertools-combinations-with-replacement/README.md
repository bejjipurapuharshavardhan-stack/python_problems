# itertools.combinations_with_replacement()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

__[itertools.combinations_with_replacement(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations_with_replacement)__  
This tool returns $r$ length subsequences of elements from the input iterable allowing individual elements to be _repeated more than once_.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

<sub> __Sample Code__ </sub>

    >>> from itertools import combinations_with_replacement
    >>> 
    >>> print list(combinations_with_replacement('12345',2))
    [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
    >>> 
    >>> A = [1,1,3,3,3]
    >>> print list(combinations(A,2))
    [(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
    
---
__Task__

You are given a string $S$.  
Your task is to print all possible size $k$ replacement combinations of the string in lexicographic sorted order.

**Input Format**

A single line containing the string $S$ and integer value $k$ separated by a space.

__Constraints__

$0<k≤len(S)$  
The string contains only *UPPERCASE* characters.

**Output Format**

 Print the combinations with their replacements of string $S$ on separate lines.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T15:48:39.753Z  

```py
from itertools import combinations_with_replacement

S, k = input().split()

for combo in combinations_with_replacement(sorted(S), int(k)):
    print("".join(combo))




```

---

[View on HackerRank](https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem)