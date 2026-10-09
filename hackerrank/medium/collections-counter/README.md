# collections.Counter()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

__[collections.Counter()](https://docs.python.org/2/library/collections.html#collections.Counter)__  
 A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
 
 <sub> __Sample Code__ </sub>
 
    >>> from collections import Counter
    >>> 
    >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    >>> print Counter(myList)
    Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    >>>
    >>> print Counter(myList).items()
    [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
    >>> 
    >>> print Counter(myList).keys()
    [1, 2, 3, 4, 5]
    >>> 
    >>> print Counter(myList).values()
    [3, 4, 4, 2, 1]

---
__Task__

$Raghu$ is a shoe shop owner. His shop has $X$ number of shoes.  
He has a list containing the size of each shoe he has in his shop.  
There are $N$ number of customers who are willing to pay $x_i$ amount of money only if they get the shoe of their desired size.

Your task is to compute how much money $Raghu$ earned.

**Input Format**

The first line contains $X$, the number of shoes.  
The second line contains the space separated list of all the shoe sizes in the shop.<br>
The third line contains $N$, the number of customers.  
The next $N$ lines contain the space separated values of the $shoe \ size$ desired by the customer and $x_i$, the price of the shoe.

__Constraints__

$0 < X < 10^3$  
$0 < N \le 10^3$  
$20 < x_i < 100$  
$ 2 < shoe \ size < 20 $
 

**Output Format**

 Print the amount of money earned by $Raghu$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T07:18:53.738Z  

```py
from collections import Counter

shoes_num = int(input())
my_list = list(map(int, input().split()))
customers = int(input())

total_revenue = 0
# Change the square brackets to parentheses here:
inventory = Counter(my_list)

for _ in range(customers):
    size, prize = map(int, input().split())
    if inventory[size] > 0:
        total_revenue += prize
        inventory[size] -= 1

print(total_revenue)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/collections-counter/problem)