# Zipped!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

__[zip([iterable, ...])](https://docs.python.org/2/library/functions.html#zip)__

This function returns a list of tuples. The $i$<sup>th</sup> tuple contains the $i$<sup>th</sup> element from each of the argument sequences or iterables. 

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence. 

<sub>__Sample Code__</sub>

    >>> print zip([1,2,3,4,5,6],'Hacker')
    [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
    >>> 
    >>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
    [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
    >>> 
    >>> A = [1,2,3]
    >>> B = [6,5,4]
    >>> C = [7,8,9]
    >>> X = [A] + [B] + [C]
    >>> 
    >>> print zip(*X)
    [(1, 6, 7), (2, 5, 8), (3, 4, 9)]

---

__Task__

The National University conducts an examination of $N$ students in $X$ subjects.  
Your task is to compute the *average scores* of each student.

$$ Average \ score = \frac{Sum \ of \ scores \ obtained \ in \ all \ subjects \ by \ a \ student}{Total \ number \ of \ subjects}$$

The format for the general mark sheet is:

	Student ID → ___1_____2_____3_____4_____5__               
    Subject 1   |  89    90    78    93    80
    Subject 2   |  90    91    85    88    86  
    Subject 3   |  91    92    83    89    90.5
                |______________________________
    Average        90    91    82    90    85.5 

**Input Format**

 The first line contains $N$ and $X$ separated by a space.  
The next $X$ lines contains the space separated marks obtained by students in a particular subject. 
 
__Constraints__

$0 \lt N \le 100 $  
$0 \lt X \le 100 $

**Output Format**

 Print the averages of all students on separate lines.
 
The averages must be correct up to $1$ decimal place.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T18:14:56.785Z  

```py
# 1. Get the number of students (N) and subjects (X)
first_line = input().split()
N = int(first_line[0])
X = int(first_line[1])

# 2. Read the scores for each subject and save them
all_scores = []
for i in range(X):
    subject_marks = list(map(float, input().split()))
    all_scores.append(subject_marks)

# 3. zip(*all_scores) groups each student's marks together
for student_marks in zip(*all_scores):
    total_score = sum(student_marks)
    average = total_score / X
    print(average)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/zipped/problem)