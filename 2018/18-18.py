ydf = open('18-19.txt','r').read().split('\n')
# Trick to part b, calculate the lum*tree figure for each minute, store in an array, at each minute check back to see if 
# the lum*tree figure has occurred before. When a repeat is found workout the cycle time (mine was 28 minutes).  Extrapolate to a billion minutes.
def gcoord(x,y,yd):
    if x < 0:
        return ''
    if y < 0:
        return ''
    if y > len(yd[0])-1:
        return ''
    if x > len(yd)-1:
        return ''
    return yd[y][x]

def threetrees(x,y,yd):
    treect = 0
    if gcoord(x+1,y,yd) == '|':
       treect += 1
    if gcoord(x,y+1,yd) == '|':
       treect += 1
    if gcoord(x,y-1,yd) == '|':
       treect += 1
    if gcoord(x-1,y,yd) == '|':
       treect += 1
    if gcoord(x+1,y+1,yd) == '|':
       treect += 1
    if gcoord(x-1,y+1,yd) == '|':
       treect += 1
    if gcoord(x+1,y-1,yd) == '|':
       treect += 1
    if gcoord(x-1,y-1,yd) == '|':
       treect += 1
    return treect
    
def threelumber(x,y,yd):
    treect = 0
    if gcoord(x+1,y,yd) == '#':
       treect += 1
    if gcoord(x,y+1,yd) == '#':
       treect += 1
    if gcoord(x,y-1,yd) == '#':
       treect += 1
    if gcoord(x-1,y,yd) == '#':
       treect += 1
    if gcoord(x+1,y+1,yd) == '#':
       treect += 1
    if gcoord(x-1,y+1,yd) == '#':
       treect += 1
    if gcoord(x+1,y-1,yd) == '#':
       treect += 1
    if gcoord(x-1,y-1,yd) == '#':
       treect += 1
    return treect
    
yd = []
ydc =[]
for y in ydf:
  line = []
  for u in y:
    line.append(u)
  yd.append(line)
prev = 0
found = False
n = 0
while not found:
 n += 1
 ydcpy =[]
 for l in yd:
  ydcpy.append(l[:])
 for y in range(len(yd)):
  for x in range(len(yd[y])):
    if threetrees(x,y,yd) > 2:
      ydcpy[y][x] = '|'
    if threelumber(x,y,yd) > 2 and \
      yd[y][x] == '|':
      ydcpy[y][x] = '#'
    if yd[y][x] == '#':
     if threelumber(x,y,yd) > 0 and \
       threetrees(x,y,yd) > 0 and \
       yd[y][x] == '#':
      ydcpy[y][x] = '#'
     else:
      ydcpy[y][x] = '.'
 yd =[]
 for l in ydcpy:
  yd = ydcpy[:]
 
 lum = 0
 tree = 0
 for g in yd:
  for j in g:
      if j == '#':
          lum += 1
      if j == '|':
          tree += 1
 ydc.append([n,lum*tree])
 cycle = -1
 epoch = -1
 l = len(ydc)
 if l > 600 and cycle == -1:
   for i in range(1,l):
    if ydc[(l-1)-i][1] == ydc[l-1][1]:
     if cycle == -1:
      cycle = i
      epoch = n
 if cycle != -1:
   if n == ((1000000000 - epoch) % cycle) + epoch:
        print 'part 2 -', lum*tree
        found = True
 if n == 10:
      print 'part 1 -', lum * tree
