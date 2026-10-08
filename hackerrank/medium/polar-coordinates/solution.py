import cmath

# Read the input string and convert it to a complex number
z = complex(input().strip())

# Calculate and print the modulus (r)
print(abs(z))

# Calculate and print the phase angle (phi)
print(cmath.phase(z))  #math.degrees  -> if need in only degrees
