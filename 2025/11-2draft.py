
f = open('ex.txt').read().split('\n')

# works for example, need to see what tricks they are up to

rl = {}
for r in f:
    st = r.split(':')[0]
    es = r.split(':')[1].split()
    rl[st] = es

#for i in rl.items():
   # print(i)

Q = [['svr',[]]]

tly = 0
SEEN = []

while Q:
    pl,pt = Q.pop()
    #print(pl,pt[:-1])
    if pl == 'out':
        #print(pt)
        if 'dac' in pt and 'fft' in pt:
            tly += 1
        continue
    if pl in pt[:-1]:
        #print(pl,pt[:-1])
        continue
    if pl in rl.keys():
        for i in rl[pl]:
            npt = pt[:]
            if True: # i in ['dac','fft']:
                npt.append(i)
            Q.append([i,npt])

print(tly)
