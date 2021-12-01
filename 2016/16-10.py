f = open('16-10.txt').read().split('\n')

bt = [[0,0] for i in range(len(f))]
o = [0 for i in range(len(f))]

def badd(b,v):
    if bt[b][1] == 0:
       bt[b][1] = v
    else:
       bt[b][0] = v
    bt[b].sort()

for r in f:
    d = r.split()
    if 'value' in r:
      v = int(d[1])
      b = int(d[-1])
      badd(b,v)

fd = False
fd1 = False
while not fd:
  for r in f:
    d = r.split()
    if 'gives' in r:
      bb = int(d[1])
      if 0 not in bt[bb]:
        for hl in [0,1]:
         b = int(d[6+(hl*5)])
         ob = d[5+(hl*5)]
         if 'out' in ob:
           o[b] = bt[bb][hl]
         else:
           badd(b,bt[bb][hl])
         bt[bb][hl] = 0

    if [17,61] in bt:
     if not fd1:
      fd1 = True
      for g in range(len(bt)):
        if [17,61] == bt[g]:
           print 'part 1 -',g
    if 0 not in o[0:3]:
        print'part 2 -',o[0]*o[1]*o[2]
        fd = True
        break
