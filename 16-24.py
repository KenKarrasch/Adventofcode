import itertools
import copy

f = open('16-24.txt').read().split('\n')

ad = [[0,1],[0,-1],[1,0],[-1,0]]
g = []
for x in f:
  ln = []
  for y in range(len(x)):
     ln.append(x[y])
  g.append(ln)
n = []
for i in range(len(g[0])):
  for j in range(len(g)):
    if g[j][i] in '0123456789':
        n.append([g[j][i],i,j])
n.sort()

def getdist(a,b):
    gn = copy.deepcopy(g)
    gn[n[a][2]][n[a][1]] = '0'
    gn[n[b][2]][n[b][1]] = 'X'
    dst = 1
    bn = [[n[a][2],n[a][1]]]
    adj = copy.deepcopy(bn)
    while True:
      mkr = str(dst)[-1]
      nadj = []
      for i in range(1,len(gn[0])-1):
       for j in range(1,len(gn)-1):
        if [j,i] in adj:
         for a in ad:
          [y,x] = [j+a[0],i+a[1]]
          if gn[y][x] not in '#X':
           if [y,x] not in bn:
              bn.append([y,x])
              nadj.append([y,x])
              gn[y][x] = mkr
          if gn[y][x] == 'X':
            return dst
      dst += 1
      adj = copy.deepcopy(nadj)
      
bk = {}
for k in range(len(n)):
  for m in range(k):
     d = getdist(k,m)
     bk[k,m] = d
     bk[m,k] = d
     print k,'to',m,'=',d
     
pts = itertools.permutations(range(1,len(n)))
ds = []
for i in pts:
  d = 0
  d += bk[(0,i[0])]
  for u in range(len(i)-1):
    d += bk[(i[u],i[u+1])]
  ds.append([d,i])

ds.sort()
print 'part 1 -',ds[0][0]

pts = itertools.permutations(range(len(n)))

ds = []
for i in pts:
  d = 0
  for u in range(len(i)-1):
    d += bk[(i[u],i[u+1])]
  d += bk[(i[0],i[len(i)-1])]
  ds.append([d,i])
ds.sort()
print 'part 2 -',ds[0][0]
