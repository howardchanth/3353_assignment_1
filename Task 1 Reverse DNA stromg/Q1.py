# Question 1 Reverse Complement of a DNA string

def substitute(c):
    if c == 'T':
        c = 'A'
    elif c == 'A':
        c = 'T'
    elif c == 'C':
        c = 'G'
    elif c == 'G':
        c = 'C'

    return c


with open("input.txt", "r") as file:
    line = file.readline()

# Reverse line
line = line[::-1]

# Join output lists into string
line = ''.join([substitute(c) for c in line])

# Save output
with open("output.txt", "w") as file:
    print(line, file=file)
