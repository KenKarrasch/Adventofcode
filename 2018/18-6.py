
def findcl(x,y,gr,b):
    min = 100000
    lt = '.'
    for i in range(len(b)):
       dx = int(b[i].split(',')[0]) - x
       if dx < 0:
           dx = -dx
       dy = int(b[i].split(',')[1]) - y
       if dy < 0:
           dy = -dy
       dist = dx + dy
       if dist == min:
           lt = '.'
       if dist < min:
           min = dist
           lt = str(i)
    return lt

def finddist(x,y,gr,b):
    min = 100000
    lt = '.'
    dist = 0
    for i in range(len(b)):
       dx = int(b[i].split(',')[0]) - x
       if dx < 0:
           dx = -dx
       dy = int(b[i].split(',')[1]) - y
       if dy < 0:
           dy = -dy
       dist = dist + dx + dy
    return dist

def printg(gr):
    for h in gr:
      str = ''
      for j in h:
        str = str + j
      print str


f = open('18-6.txt','r')
#f = open('18-6test.py','r')
b = f.read().split('\n')
s = 500

gr = [['.' for i in range(s)] for j in range(s)]

ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(b)):
    c = b[i].split(',')
    gr[int(c[0])][int(c[1])] = ch[i]
for x in range(s):
  if x%100 == 0:
   print 'searching -', x,'of', s
  for y in range(s):
    gr[x][y] = findcl(x,y,gr,b)
    
tl = [0 for u in range(50)]
inf = [0 for u in range(50)]
for x in range(s):
  for y in range(s):
    if gr[x][y] != '.':
      tl[int(gr[x][y])] = tl[int(gr[x][y])] + 1
    
for x in range(s):
    if gr[x][0] != '.':
      inf[int(gr[x][0])] = inf[int(gr[x][0])] + 1
    
for x in range(s):
    if gr[x][s-1] != '.':
      inf[int(gr[x][s-1])] = inf[int(gr[x][s-1])] + 1
    
for y in range(s):
    if gr[0][y] != '.':
      inf[int(gr[0][y])] = inf[int(gr[0][y])] + 1
      
for y in range(s):
    if gr[s-1][y] != '.':
      inf[int(gr[s-1][y])] = inf[int(gr[s-1][y])] + 1

max = 0
for i in range(len(tl)):
    if inf[i] == 0:
      if(max < tl[i]):
          max = tl[i]
    
print 'part 1 -', max


gr = [['.' for i in range(s)] for j in range(s)]
rg = [['.' for i in range(s)] for j in range(s)]

for i in range(len(b)):
    c = b[i].split(',')
    gr[int(c[0])][int(c[1])] = ch[i]

ranges = 10000
#ranges = 32
tl = [0 for u in range(50)]
inf = [0 for u in range(50)]
for x in range(s):
  if x%100 == 0:
   print 'searching -', x,'of', s
  for y in range(s):
    if finddist(x,y,gr,b) < ranges:
        rg[x][y] = '#'
ct = 0
for x in range(s):
  for y in range(s):
    if rg[x][y] != '.':
      ct = ct + 1

print 'part 2 -', ct
