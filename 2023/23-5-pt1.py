r = open('23-5.txt').read().split('\n\n')

#print r

sds = [int(y) for y in r[0].split(':')[1].split()]
#print sds
bk = []
for m in r:
    st = [[int(y) for y in x.split()] for x in m.split('\n')[1:]]
    #print st
    bk.append(st)
#print bk

def getrt(tx,n):
  for mps in bk[tx]:
    #print 'mps',mps,'tx',tx
    if n >= mps[1]:
      if n < mps[1] + mps[2]:
        #print 'tx fd',n + (mps[0] - mps[1])
        return n + (mps[0] - mps[1])
        
  return n

#print len(bk)
dst = []

#if True: #
for sd in sds:
   nn = sd

   #nn = 82
   for txl in range(len(bk)):
      #print txl
      nn = getrt(txl,nn)
      #print nn
   #print nn
   dst.append(nn)
print min(dst)
