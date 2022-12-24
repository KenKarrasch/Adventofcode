from collections import defaultdict, deque

f = open('22-23.txt').read().split('\n')

# cool air molecule motion sim

e = deque([])


for i in range(len(f)):
  for j in range(len(f[i])):
    if f[i][j] == '#':
      e.append((j,i))

#print e

def pr():
    xs = []
    ys = []
    esq = 0
    for i in e:
      xs.append(i[0])
      ys.append(i[1])
    #print xs,ys
    for j in range(1+max(ys)-min(ys)):
      st = ''
      for i in range(1+max(xs)-min(xs)):
        if (min(xs)+i,min(ys)+j) in e:
          st += '#'
        else:
          st += '_'
          esq += 1
      print st
    print '========'
    print 'part 1 -',esq




dr = [[(-1,-1),( 0,-1),( 1,-1)], \
      [(-1, 1),( 0, 1),( 1, 1)], \
      [(-1,-1),(-1, 0),(-1, 1)], \
      [( 1,-1),( 1, 0),( 1, 1)]]

#pr()

scd = 0

#for c in range(10):
dn = False
rd = 0
while not dn:
 pe = []
 kl = []
 for i in range(len(e)):
    ops = 0
    fd = False
    for dp in range(len(dr)):
       d = dr[(dp+scd)%4]
       gd = True
       for sc in d:
         sp = (e[i][0]+sc[0], \
               e[i][1]+sc[1])
         if sp in e:
           gd = False
       if gd and not fd:
           pe.append(
           (e[i][0]+d[1][0], \
            e[i][1]+d[1][1]))
           fd = True
       if gd:
           ops += 1
    if not fd:
        pe.append(None)
    if ops == 4:
        kl.append(i)
 #print kl
 for k in kl:
     pe[k] = None
 

 scd += 1
 
 #print 'pe.         ',pe
 ps = []
 for i in pe:
     if i != None:
        ps.append(i)
 #ps = [x[:] for x in pe]
 ps.sort()
 #print 'pe sorted',ps
 dup = []


 for i in range(len(ps)-1):
  if ps[i] == ps[i+1]:
    dup.append(ps[i])
    dup.append(ps[i+1])

 #print 'duplicates',dup

 for i in range(len(pe)):
  if pe[i] in dup:
    pe[i] = None

 #print pe
 
 mv = False
 for i in pe:
     if i != None:
         mv = True
 if not mv:
     print 'part 2 -',rd + 1
     dn = True
 rd += 1

 for i in range(len(e)):
  if pe[i] != None:
      e[i] = pe[i]
      
 if rd == 10:
   pr()
