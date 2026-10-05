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
