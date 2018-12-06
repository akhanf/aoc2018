import numpy as np

#read input file
infile = 'input.txt'
f = open(infile)
lines = f.readlines()
N = len(lines)

#parse input first

#datatype to contain all info from a line (event coded as guard ID if >0, 0 fall asleep, -1 wake up)
dtype_log = [('month', int), ('day', int), ('hour', int), ('minute', int),('event',int)]


log = np.empty(N, dtype_log)

#f
for i in range(0, len(lines)):

    log[i]['month'] = lines[i][6:8]
    log[i]['day'] = lines[i][9:11]
    log[i]['hour'] = lines[i][12:14]
    if log[i]['hour'] == 0:
        log[i]['hour'] = 24
    log[i]['minute'] = lines[i][15:17]
    eventstr = lines[i][19:-1]
    if eventstr == 'wakes up':
        log[i]['event'] = -1
    elif eventstr == 'falls asleep':
        log[i]['event'] = 0
    else:
        log[i]['event'] = eventstr.split()[1][1:]

#sort by time
log = np.sort(log,order = ('month', 'day', 'hour'))

#get events with id
startinds = np.nonzero(log[:]['event'] > 0)[0]

M = len(startinds)
ids = np.zeros(M,int)
nights = np.zeros((M, 60), int)

for i in range(0, M):
    id_ind = startinds[i]
    ids[i] = log[id_ind]['event']

    if i == M-1:
        next_id_ind = N
    else:
        next_id_ind = startinds[i+1]

    iter=id_ind+1
    while iter+1 <next_id_ind:
        nights[i][log[iter]['minute']:log[iter+1]['minute']] = 1
        iter = iter+2


guardset=list(set(ids))
guarddict=dict()
minutes_asleep=np.zeros(len(guardset))
for i in range(1,len(guardset)):
    guarddict[guardset[i]] = nights[ids==guardset[i]][:]
    minutes_asleep[i]=sum(sum(guarddict[guardset[i]] ))

#get guard that slept the most
sleepy = guardset[np.argmax(minutes_asleep)]

sleepy_minute=np.argmax(sum(guarddict[sleepy]))

print('answer for part 1: {}'.format(sleepy * sleepy_minute))


#part 2:
consistent_minutes=np.zeros(len(guardset))

for i in range(1,len(guardset)):
    consistent_minutes[i]=max(sum(guarddict[guardset[i]]))

con_sleepy = guardset[np.argmax(consistent_minutes)]

con_sleepy_minute=np.argmax(sum(guarddict[con_sleepy]))
print('answer for part 2: {}'.format(con_sleepy*con_sleepy_minute))
#total_slept = np.sum(nights, 1)
#print('answer for part 1: {}'.format(ids[np.argmax(total_slept)] * np.max(total_slept)))