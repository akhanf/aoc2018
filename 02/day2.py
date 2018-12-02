#read input file
infile = 'input.txt'
f = open(infile)
lines = f.readlines()

#individual checksums
sum2 = 0
sum3 = 0

for i in range(0, len(lines)):
    boxid = lines[i]

    #brute force -- count all occurrences of each char
    counts = dict()
    for j in range(0, len(boxid)-1): #leave newline out by going to len-1
        key = boxid[j]
        if key in counts:
            counts[key] = counts[key]+1
        else:
            counts[key] = 1

    #now check values
    if 2 in list(counts.values()):
        sum2 = sum2+1

    if 3 in list(counts.values()):
        sum3 = sum3+1

print('part1: final checksum = {}'.format(sum2*sum3))


