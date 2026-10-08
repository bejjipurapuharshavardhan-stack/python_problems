# Iterables and Iterators

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The _itertools_ module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an _iterator algebra_ making it possible to construct specialized tools succinctly and efficiently in pure _Python_. 

To read more about the functions in this module, check out their [documentation here](https://docs.python.org/2/library/itertools.html). 

You are given a list of $N$ lowercase English letters. For a given integer $K$, you can select any $K$ indices (assume $1$-based indexing) with a uniform probability from the list.  

Find the _probability_ that _at least_ one of the $K$ indices selected will contain the letter: '$a$'.  


**Input Format**

The input consists of three lines. The first line contains the integer $N$, denoting the length of the list. The next line consists of $N$ space-separated lowercase English letters, denoting the elements of the list. 

The third and the last line of input contains the integer $K$, denoting the number of
indices to be selected. 


**Output Format**

Output a single line consisting of the _probability_ that _at least_ one of the $K$ indices selected contains the letter:'$a$'. 

**Note**: The answer must be correct up to 3 decimal places. 


**Constraints**

$1 \le N \le 10$

$1 \le K \le N$

*All the letters in the list are lowercase English letters.*


**Sample Input**

    4 
    a a c d
    2
    



**Sample Output**

	0.8333


**Explanation**

All possible unordered tuples of length $2$ comprising of indices from $1$ to $4$ are:

$(1,2) , (1,3) , (1,4) , (2,3) , (2,4) , (3,4) $ 

Out of these $6$ combinations, $5$ of them contain either index $1$ or index $2$ which are the indices that contain the letter '$a$'. 

Hence, the answer is $\frac{5}{6}$.

<!-- Note: Considering ordered tuples(permutations) would not change the answer as -->

<!-- both the numerator and the denominator in the probability would be doubled. -->

**Input Format**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T16:34:09.658Z  

```py
from itertools import combinations

list_size = int(input())
my_list = input().lower().split()
K = int(input())

total = 0
good = 0
for combo in combinations(my_list, K):
    total += 1
    if 'a' in combo:
        good += 1

print(round(good / total, 4))





```

---

[View on HackerRank](https://www.hackerrank.com/challenges/iterables-and-iterators/problem)