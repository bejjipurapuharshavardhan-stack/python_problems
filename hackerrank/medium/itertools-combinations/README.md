# itertools.combinations()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

__[itertools.combinations(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations)__  
This tool returns the $r$ length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

<sub> __Sample Code__ </sub>

    >>> from itertools import combinations
    >>> 
    >>> print list(combinations('12345',2))
    [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
    >>> 
    >>> A = [1,1,3,3,3]
    >>> print list(combinations(A,4))
    [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
    
---

__Task__

You are given a string $S$.  
Your task is to print all possible combinations, up to size $k$, of the string in lexicographic sorted order.

**Input Format**

A single line containing the string $S$ and integer value $k$ separated by a space.

__Constraints__
 
$0<k≤len(S)$  
The string contains only *UPPERCASE* characters.

**Output Format**

Print the different combinations of string $S$ on separate lines.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T07:39:51.374Z  

```py
from itertools import combinations

S, k = input().split()

for i in range(1, int(k) + 1):
    # Generate combinations of size i using the sorted string
    for c in combinations(sorted(S), i):
        print("".join(c))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/itertools-combinations/problem)