# Polar Coordinates

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

[__Polar coordinates__](https://en.wikipedia.org/wiki/Polar_coordinate_system) are an alternative way of representing Cartesian coordinates or [Complex Numbers](https://en.wikipedia.org/wiki/Complex_number).

A complex number $z$ 
<img src="http://i.picresize.com/images/2015/08/21/OUzGu.png" title="Capture.PNG"/>
$$z = x + yj$$
is completely determined by its real part $x$ and imaginary part $y$.  
Here, $j$ is the [imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit).


A polar coordinate ($r , φ$)
<img src="https://s3.amazonaws.com/hr-challenge-images/9951/1440141121-5b051fd241-Capture.PNG" title="Capture.PNG" />

is completely determined by modulus $r$ and phase angle $φ$.<br><br>
If we convert complex number $z$ to its polar coordinate, we find:<br>
$r$: Distance from $z$ to origin, i.e., $\sqrt{x^2 + y^2}$<bR>
$φ$: Counter clockwise angle measured from the positive $x$-axis to the line segment that joins $z$ to the origin.

Python's [cmath](https://docs.python.org/2/library/cmath.html) module provides access to the mathematical functions for complex numbers.

$cmath.phase$  
This tool returns the phase of complex number $z$ (also known as the argument of $z$).
```python2
>>> phase(complex(-1.0, 0.0))
3.1415926535897931
```  
$abs$  
This tool returns the modulus (absolute value) of complex number $z$.
```python2
>>> abs(complex(-1.0, 0.0))
1.0
```
  
__Task__  
You are given a complex $z$. Your task is to convert it to polar coordinates.


**Input Format**

 A single line containing the complex number $z$. 
 Note: complex() function can be used in python to convert the input as a complex number.

**Constraints**

Given number is a valid complex number

**Output Format**

Output two lines:
<br> The first line should contain the value of $r$.
<br> The second line should contain the value of $φ$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T18:18:58.620Z  

```py
import cmath

# Read the input string and convert it to a complex number
z = complex(input().strip())

# Calculate and print the modulus (r)
print(abs(z))

# Calculate and print the phase angle (phi)
print(cmath.phase(z))  #math.degrees  -> if need in only degrees

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/polar-coordinates/problem)