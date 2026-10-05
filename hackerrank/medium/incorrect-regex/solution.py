# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

test_cases = int(raw_input())

for _ in range(test_cases):
    pattern = raw_input()
    try:
        re.compile(pattern)
        print True
    except re.error:
        print False
