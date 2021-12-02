def getpl(c,sn):
  rid = c[0] + 10
  bpl = rid * c[1]
  npl = bpl + sn
  nnpl = rid * npl
  hd = int(str(nnpl)[-3:-2])
  pl = hd - 5
  return pl

sn = int(open('18-11.txt','r').read())

tw = [[0 for i in range(300)] for j in range(300)]

sw = [[0 for i in range(300)] for j in range(300)]

for i in range(300):
  for j in range(300):
    tw[i][j] = getpl([i,j],sn)
for i in range(300):
  for j in range(300):
    sw[i][j] = tw[i][j]
max = -1000000
c = [0,0]
szm = 0
run = 0
for sz in range(1,300):
 prev = szm
 for i in range(301 - sz):
  for j in range(301 - sz):
    tl = 0
    for k in range(sz):
      sw[i][j] += tw[i+k][j+sz-1]
    for l in range(sz):
      sw[i][j] += tw[i+sz-1][j+l]
    sw[i][j] -= tw[i+sz-1][j+sz-1]
    tl = sw[i][j]
    if tl > max:
       c = [i,j]
       max = tl
       szm = sz
 if prev == szm:
     run += 1
 if sz == 3:
   print 'part 1 -', c
 if run == 8:
   print 'part 2 -', c[0],',',c[1],',',szm
