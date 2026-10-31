import math

ab = int(input())
bc = int(input())

angle = round(math.degrees(math.atan2(ab, bc)))
print(f"{angle}{chr(176)}")
