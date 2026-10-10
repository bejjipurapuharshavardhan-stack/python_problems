# Collections.OrderedDict()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

###<sub>[collections.OrderedDict](https://docs.python.org/2/library/collections.html#ordereddict-objects)</sub>

An *OrderedDict* is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged. 

__Example__

<sub>__Code__</sub>

    >>> from collections import OrderedDict
    >>> 
    >>> ordinary_dictionary = {}
    >>> ordinary_dictionary['a'] = 1
    >>> ordinary_dictionary['b'] = 2
    >>> ordinary_dictionary['c'] = 3
    >>> ordinary_dictionary['d'] = 4
    >>> ordinary_dictionary['e'] = 5
    >>> 
    >>> print ordinary_dictionary
    {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
    >>> 
    >>> ordered_dictionary = OrderedDict()
    >>> ordered_dictionary['a'] = 1
    >>> ordered_dictionary['b'] = 2
    >>> ordered_dictionary['c'] = 3
    >>> ordered_dictionary['d'] = 4
    >>> ordered_dictionary['e'] = 5
    >>> 
    >>> print ordered_dictionary
    OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

---
__Task__  

You are the manager of a supermarket.  
You have a list of $N$ items together with their prices that consumers bought on a particular day.  
Your task is to print each `item_name` and `net_price` in order of its first occurrence.  

<sub>`item_name` = Name of the item.</sub>  
<sub>`net_price` = Quantity of the item sold multiplied by the price of each item.</sub>


**Input Format**

The first line contains the number of items, $N$.  
The next $N$ lines contains the item's name and price, separated by a space.

__Constraints__

$ 0 < N \le 100$

**Output Format**

Print the `item_name` and `net_price` in order of its first occurrence.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T16:21:01.423Z  

```py
from collections import OrderedDict

n = int(input())

sales = OrderedDict()

for _ in range(n):
    data = input().split()
    
    price = int(data[-1])
    
    item_name = " ".join(data[:-1])
    
    if item_name in sales:
        sales[item_name] += price
    else:
        sales[item_name] = price

for item, net_price in sales.items():
    print(f"{item} {net_price}")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-collections-ordereddict/problem)