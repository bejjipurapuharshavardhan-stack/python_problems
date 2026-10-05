# Exceptions

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

###<sub>[Exceptions](https://docs.python.org/2/tutorial/errors.html#exceptions)</sub>   
Errors detected during execution are called *exceptions*.

**Examples**:

[__*ZeroDivisionError*__](https://docs.python.org/2/library/exceptions.html#exceptions.ZeroDivisionError)  
This error is raised when the second argument of a division or modulo operation is zero.

```python
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
```
    
[__*ValueError*__](https://docs.python.org/2/library/exceptions.html#exceptions.ValueError)   
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value. 

```python
>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
```
    
<sub> To learn more about different built-in exceptions __[click here](https://docs.python.org/2/library/exceptions.html#module-exceptions)__.</sub>    
###<sub>[Handling Exceptions](https://docs.python.org/2/tutorial/errors.html#handling-exceptions)</sub>    

The statements *try* and *except* can be used to handle selected exceptions. A *try* statement may have more than one except clause to specify handlers for different exceptions.

```python
#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
```

**Output**

Error Code: integer division or modulo by zero
    
---
__Task__

You are given two values $a$ and $b$.  
Perform integer division and print $a/b$. 


**Input Format**

The first line contains $T$, the number of test cases.  
The next $T$ lines each contain the space separated values of $a$ and $b$.

__Constraints__

* $0 < T < 10$

**Constraints**

 

**Output Format**

Print the value of $a/b$.  
In the case of *ZeroDivisionError* or *ValueError*, print the error code.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T16:43:42.989Z  

```py
test_cases = int(input())

for _ in range(test_cases):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError:
        # Explicitly match the expected output
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        # ValueError's default string already matches perfectly
        print("Error Code:", e)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/exceptions/problem)