import numpy as np

#read input file
infile = 'input.txt'
f = open(infile)
lines = f.readlines()

boxlist=[]

for i in range(0, len(lines)):
    boxlist.append([ord(x) for x in lines[i]])

#now convert list to numpy array
boxarray=np.array(boxlist)

#now, can loop through
for i in range(0,boxarray.shape[0]):
    for j in range(0,boxarray.shape[0]):
        if i != j:
            #get number of mismatches, by getting the abs difference between
            #the numeric representations, and setting each diff to 1, and sum

            diff_inds=np.where(abs(boxarray[i] - boxarray[j]) > 0, 1, 0)

            if sum(diff_inds) == 1:
                #check which chars are the same, by picking out indices with 0
                # difference, and converting those back to char, creating a list
                # and joining into a string
                matchinglist=list([chr(x) for x in boxarray[i, diff_inds < 1]])
                print('list of matching chars: {}'.format(''.join(matchinglist)))
                break



