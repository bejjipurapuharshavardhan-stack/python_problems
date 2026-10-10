# Collections.namedtuple()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

###<sub>__[collections.namedtuple()](https://docs.python.org/2/library/collections.html#collections.namedtuple)__</sub>  

Basically, _namedtuples_ are easy to create, lightweight object types.  
They turn tuples into convenient containers for simple tasks.  
With *namedtuples*, you don’t have to use integer indices for accessing members of a tuple.


**Example**

<sub>__Code 01__</sub>

	>>> from collections import namedtuple
    >>> Point = namedtuple('Point','x,y')
    >>> pt1 = Point(1,2)
    >>> pt2 = Point(3,4)
    >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
    >>> print dot_product
    11
    
<sub>__Code 02__</sub>

    >>> from collections import namedtuple
    >>> Car = namedtuple('Car','Price Mileage Colour Class')
    >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
    >>> print xyz
    Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
    >>> print xyz.Class
    Y

---
__Task__

Dr. John Wesley has a spreadsheet containing a list of student's $IDs$, $marks$, $class$ and $name$.  

Your task is to help Dr. Wesley calculate the average marks of the students.

<sub>$$Average = \frac{Sum \ of \ all \ marks }{ Total \ Students }$$</sub>

__<sub>Note:  
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.  
2. Column names are `ID`, `MARKS`, `CLASS` and `NAME`. (The spelling and case type of these names won't change.)</sub>__


**Input Format**

The first line contains an integer $N$, the total number of students. <br>
The second line contains the names of the columns in any order.  
The next $N$ lines contains the $marks$, $IDs$, $name$ and $class$, under their respective column names.

__Constraints__

$ 0 < N \le 100$

**Output Format**

Print the average marks of the list corrected to 2 decimal places.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T15:49:02.757Z  

```py
from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
total_marks = 0

for _ in range(n):
    row = input().split()
    student = Student(*row)
    total_marks += int(student.MARKS)

print(f"{total_marks / n:.2f}")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem)