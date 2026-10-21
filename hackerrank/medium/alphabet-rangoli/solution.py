import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join([alpha[size-1-j] for j in range(i+1)] + [alpha[size-1-j] for j in range(i-1, -1, -1)])
        lines.append(s.center(4*size-3, "-"))
    print('\n'.join(lines + lines[-2::-1]))

