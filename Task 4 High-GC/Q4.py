def count(string, conditions):
    _sum = 0
    for cond in conditions:
        _sum += string.count(cond)
    return _sum


def replace(string):
    new_string = ''
    for j in range(len(string)):
        if string[j].isupper():
            new_string += 'N'
        else:
            new_string += 'n'
    return new_string


def read_fasta(filename):
    """Read a sequence in from a FASTA file containing a single sequence.

    We assume that the first line of the file is the descriptor and all
    subsequent lines are sequence.

    ACKNOWLEDGEMENT: Source of the function is  http://justinbois.github.io/bootcamp/2019/lessons/l17_exercise_2.html
    """
    with open(filename, 'r') as f:
        # Read in descriptor
        # noinspection PyShadowingNames
        descriptor = f.readline().rstrip()

        # Read in sequence, stripping the whitespace from each line
        seq = ''
        line = f.readline().rstrip()
        while line != '':
            seq += line
            line = f.readline().rstrip()

    return descriptor, seq


# Read sequence and define k
print("Loading DNA sequence...")

descriptor, s = read_fasta("../chr22.fa")
k = 100
s_masked = s
starts = []
ends = []

print("Sequence loaded")
print("Computing GC-contents...")
# Task 1: Compute length-k substrings of s are high-GC
# Compute GC ratios and report if it is high
counter = 0
for i in range(len(s) - k):
    sub_str = s[i:i + k]
    gc_ratio = count(sub_str, "GC") / k
    if gc_ratio > 0.70:
        counter += 1
        # Mark starting and ending position of high-GC strings for task 2
        starts.append(i)
        ends.append(i + 100)

print(counter)  # 387292

print("Masking high-gc substrings...")
# Task 2: Masking high-GC substrings
count = 0
for start, end in zip(starts, ends):
    # replace the string with "N" or "n"s
    s_masked = s_masked[:start] + replace(s_masked[start:end]) + s_masked[end:]
    count += 1
    if count % 10000 == 0:
        print(f'{count} has been masked')

# Output masked DNA string to file
with open("chr22.masked.fa", "w") as file:
    print(">chr22", file=file)
    print(s_masked, file=file)
