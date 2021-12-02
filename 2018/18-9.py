def insert(c, n, data, nxt, prev):
  m[data] = n
  nxt[data] = nxt[c]
  prev[data] = c
  oldnxt = nxt[c]
  nxt[c] = data
  prev[oldnxt] = data

def remove(c, nxt, prev):  
  prev[nxt[c]] = prev[c]
  nxt[prev[c]] = nxt[c]  

def printm(pli, m, prev, nxt, data):
  marble = []
  cind = 0
  for i in range(data + 1):
    marble.append(m[cind])
    cind = nxt[cind]
  print pli, marble

s = open('18-9.txt').read().split()
players = int(s[0])
end = int(s[6])
c = 0
pl = [0 for i in range(players)]
nxt = [0 for i in range(end)]
prev = [0 for i in range(end)]
m = [0 for i in range(end)]
nxt[0] = 0
prev[0] = 0
pli = 0
data = 0
num = 0
  
for j in range(2):
 c = 0
 if j == 1: 
  end *= 100
 pl = [0 for i in range(players)]
 nxt = [0 for i in range(end)]
 prev = [0 for i in range(end)]
 m = [0 for i in range(end)]
 nxt[0] = 0
 prev[0] = 0
 pli = 0
 data = 0
 num = 0
 for i in range(end):
  pli += 1
  if pli >= len(pl):
    pli = 0
  num += 1
  if num % 23 == 0:
    c = prev[prev[prev[prev[prev[prev[c]]]]]]    
    pl[pli] += num
    pl[pli] += m[c]
    remove(c, nxt, prev)
  else:
    c = nxt[nxt[c]]
    data += 1
    insert(c, num, data, nxt, prev)     
  if i % 1000000 == 0:
    if j == 1:
      print 'Analysing ', i,'of',end
 max = 0
 for i in range(players):
    if max < pl[i]:
      max = pl[i]
 print 'part', 1 + j, '-', max
