import numpy as np

#read input file
infile = 'input.txt'
f = open(infile)
lines = f.readlines()

fab = np.zeros((1000,1000))

for i in range(0,len(lines)):
    coords=lines[i].split(' ')[2]
    xc = int(coords.split(',')[0])
    yc = int(coords.split(',')[1].split(':')[0])
    width = int(lines[i].split(' ')[3].split('x')[0])
    height = int(lines[i].split('x')[1].split('\n')[0])
    fab[xc:xc+width, yc:yc+height]=fab[xc:xc+width, yc:yc+height]+1

print('answer to part 1: {}'.format(sum(sum(fab>1))))


for i in range(0,len(lines)):
    coords=lines[i].split(' ')[2]
    xc = int(coords.split(',')[0])
    yc = int(coords.split(',')[1].split(':')[0])
    width = int(lines[i].split(' ')[3].split('x')[0])
    height = int(lines[i].split('x')[1].split('\n')[0])

    #check this against the fabric - if
    totalclaimed=sum(sum(fab[xc:xc+width, yc:yc+height]))
    if(totalclaimed == width*height):
        print('answer to part 2: {}'.format(lines[i].split(' ')[0]))

