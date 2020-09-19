import csv
# Read and combine 3 bases as codon


def read_codon(index, s):
    if index + 3  < len(s):
        return ''.join(s[index:(index + 3)])
    else:
        return None


# Map DNA codons to Standard genetic code
def map_codon(codon):
    with open("standard_genetic_table.csv", "r", newline='') as sgt:
        lines = csv.reader(sgt)
        table = []
        for l in lines:
            table.append(l)

    for l in table:
        if codon in l:
            return l[0]


with open("input.txt", "r") as file:
    s = file.readline()

start = False
index = 0
output = []

while read_codon(index, s):
    if read_codon(index, s) == 'AUG':
        start = True
    if map_codon(read_codon(index, s)) == 'STOP':
        break
    if start:
        codon = read_codon(index, s)
        output.append(map_codon(codon))
        index += 2
    index += 1

output = ''.join(output)

with open("output.txt", "w") as file:
    print(output, file=file)

