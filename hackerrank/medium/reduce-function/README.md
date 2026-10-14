# Reduce Function

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a list of rational numbers,find their product.  

**Concept**     
The `reduce()` function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say `[1,2,3]` and you have to find its sum.

```python
>>> reduce(lambda x, y : x + y,[1,2,3])
6
```


You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:

```python
>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1
```



**Input Format**

First line contains $n$, the number of rational numbers.           
The $i^{\text{th}}$ of next $n$ lines contain two integers each, the numerator( $N_i$ ) and denominator( $D_i$ ) of the $i^{\text{th}}$ rational number in the list.

**Constraints**

- $1 \le n \le 100$        
- $1 \leq N_i, D_i \leq 10^9 $

**Output Format**

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than $1$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T15:39:04.825Z  

```py

import operator

def product(fracs):
    t = reduce(operator.mul,fracs)
    return t.numerator, t.denominator


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/reduce-function/problem)