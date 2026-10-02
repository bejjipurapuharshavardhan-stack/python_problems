x, k = map(int, input().split())
polynomial_string = input()

result = eval(polynomial_string) # Evaluate the polynomial string
print(result == k)
