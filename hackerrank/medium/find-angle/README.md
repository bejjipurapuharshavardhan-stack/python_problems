# Find Angle MBC

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<img src="https://s3.amazonaws.com/hr-challenge-images/9668/1440151155-10b2b748ee-rsz_1438840048-2cf71ed69d-findangle.png" title="rsz_1438840048-2cf71ed69d-findangle.png" />
$ABC$ is a right triangle, $90°$ at $B$.<br>
Therefore, $\measuredangle ABC = 90°$.

Point $M$ is the midpoint of hypotenuse $AC$.

You are given the lengths $AB$ and $BC$. <br>
Your task is to find $\measuredangle MBC$  (angle $\theta°$, as shown in the figure) in degrees.



**Input Format**

The first line contains the length of side $AB$.<br>
The second line contains the length of side $BC$.  


**Constraints**

+ $0 < AB \leq 100$<br> 
+ $0 < BC \leq 100$
+ Lengths $AB$ and $BC$ are natural numbers.

**Output Format**

Output $\measuredangle MBC$ in degrees. <br>


**Note:** Round the angle to the nearest integer.

**Examples**:  
If angle is 56.5000001°, then output __57°__.  
If angle is 56.5000000°, then output __57°__.  
If angle is 56.4999999°, then output __56°__.  

$0° < \theta° < 90°$

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T18:34:48.620Z  

```py
import math

ab = int(input())
bc = int(input())

angle = round(math.degrees(math.atan2(ab, bc)))
print(f"{angle}{chr(176)}")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/find-angle/problem)