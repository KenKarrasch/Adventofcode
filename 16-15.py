f = open('16-15.txt').read().split('\n')

d = [[int(x.split()[1][1:]),int(x.split()[3]), \
      int(x.split()[6][5:-1]),int(x.split()[11][:-1])] for x in f]
fd,t,ds = False,0,len(d)
while not fd:
    ct = 0
    for i in range(ds):      
      if (t+d[i][0]+d[i][3]-d[i][2])%d[i][1] == 0:
        ct += 1
    if ct == ds:
        print('part 1 -',t)
        fd = True
    t += 1
fd,t = False,0
d.append([ds,11,0,1])
ds += 1
while not fd:
    ct = 0
    for i in range(ds):      
      if (t+d[i][0]+d[i][3]-d[i][2])%d[i][1] == 0:
        ct += 1
    if ct == ds:
        print('part 1 -',t)
        fd = True
    t += 1
