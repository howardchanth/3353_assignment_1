def count(string, conditions):
    c = 0
    for cond in conditions:
        c += string.count(cond)
    return c


def read_fasta(filename):
    """Read a sequence in from a FASTA file containing a single sequence.

    We assume that the first line of the file is the descriptor and all
    subsequent lines are sequence.

    ACKNOWLEDGEMENT: Source of the function is  http://justinbois.github.io/bootcamp/2019/lessons/l17_exercise_2.html
    """
    with open(filename, 'r') as f:
        # Read in descriptor
        # noinspection PyShadowingNames
        descriptor = f.readline()

        # Read in sequence, stripping the whitespace from each line
        seq = f.readline()

    return descriptor, seq


# Read sequence and define k
print("Loading DNA sequence...")

descriptor, s = read_fasta("./chr22.fa")
k = 100
s_masked = s
starts = []
ends = []
index_replace = [False] * len(s)

print("Sequence loaded")
print("Computing GC-contents...")
# Task 1: Compute length-k substrings of s are high-GC
# Compute GC ratios and report if it is high
counter = 0
for i in range(len(s) - k):
    sub_str = s[i:i + k]
    gc_ratio = count(sub_str, "GCgc") / k
    if gc_ratio > 0.70:
        # Update array indices for replacement in task 2
        for j in range(i, i + k):
            index_replace[j] = True
        counter += 1

print(f"Number of substrings having high GC-content: {counter}")  # 499917

print("Masking high-GC substrings...")
# Task 2: Masking high-GC substrings
s_masked = list(s_masked)
for i in range(len(s)):
    if index_replace[i]:
        if s_masked[i].isupper():
            s_masked[i] = 'N'
        else:
            s_masked[i] = 'n'


# Combine list of characters to string
s_masked = "".join(s_masked)

print("Masking complete!")
print("Outputting masked sequence...")
# Output masked DNA string to file
with open("./chr22.masked.fa", "w") as file:
    print(">chr22", file=file)
    print(s_masked, file=file)
