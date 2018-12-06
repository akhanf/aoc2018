import numpy as np
import string


#read input file
infile = 'input.txt'
f = open(infile)
inpolymer=f.readline()

out=list()

#add dummy to start
out.append('1')

#loop through input
for i in range(0,len(inpolymer)):
    #if lowercase(input) matches, but chars are different, then its a match:
    if out[-1].lower() == inpolymer[i].lower() and out[-1] != inpolymer[i] :
        #match, explode!
        out.pop()
    else:
        out.append(inpolymer[i])



#remove 2 (beginning dummy, and end newline)
print('part 1 answer is: {}'.format(len(out)-2))


#now
hotchar_len = dict()

for hotchar in list(string.ascii_lowercase):

    out=list()

    #add dummy to start
    out.append('1')

    # loop through input
    for i in range(0, len(inpolymer)):
        if hotchar == inpolymer[i].lower():
            continue
        # if lowercase(input) matches, but chars are different, then its a match:
        if out[-1].lower() == inpolymer[i].lower() and out[-1] != inpolymer[i]:
            # match, explode!
            out.pop()
        else:
            out.append(inpolymer[i])

    hotchar_len[hotchar] = len(out)-2

print('part 2 answer is: {}'.format(min(hotchar_len.values())))
