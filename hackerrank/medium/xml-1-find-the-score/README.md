# XML 1 - Find the Score

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has. 

**Input Format**

The first line contains $N$, the number of lines in the XML document.<br>
The next $N$ lines follow containing the XML document.

**Output Format**

Output a single line, the integer score of the given XML document.

**Sample Input**  
```xml
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
```

**Sample Output**  
```xml
5
```  
**Explanation**

The feed and subtitle tag have one attribute each - *lang*. <br>
The title and updated tags have no attributes. <br>
The link tag has three attributes - *rel, type* and *href*. <br>

So, the total score is $1 + 1 + 3 = 5$.
<br><br>
There may be any level of nesting in the XML document. To learn about XML parsing, refer [here](http://www.diveintopython3.net/xml.html).
<br>

**NOTE**: In order to parse and generate an XML element tree, use the following code:<br>

	>> import xml.etree.ElementTree as etree
	>> tree = etree.ElementTree(etree.fromstring(xml))

Here, XML is the variable containing the string.<br>
Also, to find the number of keys in a dictionary, use the *len* function:<br>

	>> dicti = {'0': 'This is zero', '1': 'This is one'}
	>> print (len(dicti))

	2

**Input Format**

 

**Constraints**

  

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T13:58:13.825Z  

```py

import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)
    for child in node:
        score += get_attr_number(child)   
    return score
    


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/xml-1-find-the-score/problem)