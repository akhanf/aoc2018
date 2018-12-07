import numpy as np

#read input file
infile = 'input.txt'
f = open(infile)

coordlines=f.readlines()

coords=np.empty((len(coordlines), 2),int)
for i in range(0, len(coordlines)):
    coords[i, 0] = coordlines[i].split(',')[0]
    coords[i, 1] = coordlines[i].split(' ')[1]

N=500
ys,xs=np.mgrid[0:N,0:N]

bigmat=np.empty((len(coords),N,N),int)
for i in range(0,len(coords)):
    bigmat[i]=abs(xs - coords[i][0]) + abs(ys - coords[i][1])

#argmax to assign mindist label to each
amin=np.argmin(bigmat,0)

#remove ties
sorted=np.sort(bigmat,0)
ties = sorted[0]==sorted[1]
amin[ties]=-1

#find boundary labels
bdyvals=np.unique(np.concatenate((amin[0,:],amin[-1,:],amin[:,0],amin[:,-1])))

#get sizes -- lazy now, it's getting late...
sizes=np.zeros(len(coords),int)

for i in range(0,len(coords)):
    if i not in bdyvals:
        sizes[i]=sum(sum(amin==i))

print('answer to part 1: {}'.format(max(sizes)))


#for part two, want to sum up the distances to all coordinates
sumdist=np.sum(bigmat,0)
print('answer to part 2: {}'.format(sum(sum(sumdist<10000))))