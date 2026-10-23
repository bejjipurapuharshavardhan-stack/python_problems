# Collections.deque()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

###<sub>[collections.deque()](https://docs.python.org/2/library/collections.html#collections.deque)</sub>  

A *deque* is a double-ended queue. It can be used to add or remove elements from both ends.  

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same $O(1)$ performance in either direction.

Click on the link to learn more about [__deque() methods__](https://docs.python.org/2/library/collections.html#deque-objects).  
Click on the link to learn more about various approaches to working with deques: [__Deque Recipes__](https://docs.python.org/2.7/library/collections.html#deque-recipes).

**Example**

<sub>__Code__</sub>

    >>> from collections import deque
    >>> d = deque()
    >>> d.append(1)
    >>> print d
    deque([1])
    >>> d.appendleft(2)
    >>> print d
    deque([2, 1])
    >>> d.clear()
    >>> print d
    deque([])
    >>> d.extend('1')
    >>> print d
    deque(['1'])
    >>> d.extendleft('234')
    >>> print d
    deque(['4', '3', '2', '1'])
    >>> d.count('1')
    1
    >>> d.pop()
    '1'
    >>> print d
    deque(['4', '3', '2'])
    >>> d.popleft()
    '4'
    >>> print d
    deque(['3', '2'])
    >>> d.extend('7896')
    >>> print d
    deque(['3', '2', '7', '8', '9', '6'])
    >>> d.remove('2')
    >>> print d
    deque(['3', '7', '8', '9', '6'])
    >>> d.reverse()
    >>> print d
    deque(['6', '9', '8', '7', '3'])
    >>> d.rotate(3)
    >>> print d
    deque(['8', '7', '3', '6', '9'])
    



---
__Task__  

Perform _append_, _pop_, _popleft_ and _appendleft_ methods on an empty deque $d$.

**Input Format**

The first line contains an integer $N$, the number of operations.  
The next $N$ lines contains the space separated names of methods and their values.  

__Constraints__

$ 0 < N \le 100$

**Output Format**

Print the space separated elements of deque $d$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:06:20.438Z  

```py
from collections import deque

d = deque()
num_oper = int(input())

for _ in range(num_oper):
    methods = input().lower().split()
    if methods[0] == 'append':
        d.append(methods[1])
    elif methods[0] == 'appendleft':
        d.appendleft(methods[1])
    elif methods[0] == 'pop':
        d.pop()
    elif methods[0] == 'popleft':
        d.popleft()

print(*d)


  

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-collections-deque/problem)