f=open("input.txt")
lines=f.readlines()
pastfreq=list()

N=len(lines)
currfreq=0

pastfreq=set()

while 1:
    for i in range(0,N,1):
        currfreq=currfreq+int(lines[i])
        szbefore=len(pastfreq)
        pastfreq.add(currfreq)
        szafter=len(pastfreq)
        if (szbefore==szafter):
            print(currfreq)
            exit(0)

