import re

for _ in range(int(input())):
    try:
        val = input()
        print(bool(re.match(r"^[\+\-]?\d*\.\d+$", val)) and not (val.count('.') > 1))
    except ValueError:
        print(False)
