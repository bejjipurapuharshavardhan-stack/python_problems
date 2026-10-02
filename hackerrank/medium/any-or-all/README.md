# Any or All

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

###<sub>[any()](https://docs.python.org/2/library/functions.html#any)</sub>  
This expression returns `True` if __any__ element of the iterable is true.  
If the iterable is empty, it will return `False`. 

<sub>__Code__</sub>
	
    >>> any([1>0,1==0,1<0])
    True
    >>> any([1<0,2<1,3<2])
    False

---
###<sub>[all()](https://docs.python.org/2/library/functions.html#all)</sub>    
This expression returns `True` if __all__ of the elements of the iterable are true. If the iterable is empty, it will return `True`. 

<sub>__Code__</sub>  

	>>> all(['a'<'b','b'<'c'])
    True
    >>> all(['a'<'b','c'<'b'])
    False
    
--- 
__Task__

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a [palindromic integer](https://en.wikipedia.org/wiki/Palindromic_number).

**Input Format**

The first line contains an integer $N$. $N$ is the total number of integers in the list.  
The second line contains the space separated list of $N$ integers.

__Constraints__

$ 0 < N < 100$


**Output Format**

Print `True` if all the conditions of the problem statement are satisfied. Otherwise, print `False`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T21:37:04.254Z  

```py
num = int(input())
list1 = list(map(int,input().split()))

print(True)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/any-or-all/problem)