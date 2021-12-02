s = open('20-5.txt').read().split('\n')

# another good one for the kids, did part 1 while christmas shopping

sts, sl = [],[]
er = [0,0,0,0,0,0,0,0]
for i in range(128):
    sl.append(er[:])
for i in s:
    m, st, r = 1,0,0
    for j in [6,5,4,3,2,1,0]:
        if i[j]== 'B':
           r += m
        m *= 2
    m = 1
    for j in [9,8,7]:
        if i[j] == 'R':
           st += m
        m *= 2
    sts.append(r*8+st)
    sl[r][st] = 1
    
print 'part 1 -',max(sts)

p, fd = -1, False
for i in range(128):
    for j in range(8):
        if sl[i][j] == 0:
          if not fd:
            if p+1 != i*8+j:
                print 'part 2 -',i*8+j
                fd = True
            p += 1
