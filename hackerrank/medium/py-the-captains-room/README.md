# The Captain's Room

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Mr. Anant Asankhya is the manager at the *INFINITE* hotel. The hotel has an infinite amount of rooms. 

One fine day, a *finite* number of tourists come to stay at the hotel. <br>
The tourists consist of:<br>
&#8594; A Captain.<br>
&#8594; An unknown group of families consisting of $K$ members per group where $K$ &#x2260; $1$.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear $K$ times per group except for the Captain's room. 

Mr. Anant needs you to help him find the Captain's room number.
<br>*The total number of tourists or the total number of groups of families is not known to you.*
<br>*You only know the value of $K$ and the room number list.*

**Input Format**

The first line consists of an integer, $K$, the size of each group.<br>
The second line contains the unordered elements of the room number list.<br>
<br>

__Constraints__

$1 < K < 1000 $

**Output Format**

Output the Captain's room number.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T18:26:49.755Z  

```py
K = int(input())
my_list = list(map(int, input().split()))

my_list.sort()
n = len(my_list)

i = 0
while i < n:
    j = i
    while j < n and my_list[j] == my_list[i]:
        j += 1
    if j - i != K:
        print(my_list[i])
        break
    i = j










      



```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-the-captains-room/problem)