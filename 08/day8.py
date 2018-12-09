import numpy as np
from collections import deque



#read input file
infile = 'input.txt'
f = open(infile)
inline = f.readline()
#for testing:
#nplayers = 30
#lastmarble = 5807

nplayers = int(inline.split(' ')[0])
lastmarble = int(inline.split(' ')[-2])

for part in (1,2):
    if (part==2):
        lastmarble = lastmarble*100

    #make a deque, max size=lastmarble


    D = deque(maxlen=lastmarble)
    scores = np.zeros(nplayers,int)

    #add first marble
    D.append(0)

    #current marble position
    currpos = 0

    #iterate through turns of the game, i is marble number
    for i in range(1, lastmarble+1):
        player=(i-1)%nplayers # players from 0 to nplayers-1

      #for debugging:
      #  print('curr marble {} at position {}, curr player {}'.format(i,currpos,player))

        if (i%23 == 0):
            #marble is multiple of 23, player keeps it
            scores[player] = scores[player] + i
            #want to remove marble 7 marbles counter-clockwise (negative dir) to it
            #want to rotate so that currpos is +7
            D.rotate(7-currpos)
            scores[player] = scores[player]+D.popleft()
            currpos = 0
        else:
            #position to insert (currpos+1 is clockwise neighbour), then new pos is +1 of that
            currpos=(currpos+1)%len(D) + 1
            D.insert(currpos,i)


    #max score:
    print('answer to part {}: {}'.format(part,np.max(scores)))
