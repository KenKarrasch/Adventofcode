f = open('18-17.txt','r').read().split('\n')

mins = [10000,10000]
maxs = [-10000,-10000]
x,y = 0,0
L,R = -1,1
top = 0
g = [['.' for i in range(2000)] for j in range(1000)]

def printclay():
  count = 0
  clay = 0
  for i in range(2000):
    strr = ''
    for gr in range(len(g[0][mins[0]:maxs[0]])):
      strr += g[gr+mins[0]][i+mins[1]]
      if g[gr+mins[0]][i+mins[1]] in '|~':
        if i > top:
          count += 1
      if g[gr+mins[0]][i+mins[1]] in '~':
        if i > top:
          clay += 1      
  print 'part 1 -',count
  print 'part 2 -',clay

def fillclay(lr):
  xt = x
  while g[xt-lr][y] == '~':
        g[xt-lr][y] = '|'
        xt -= lr

def findwaterfall(lr):
  global x
  while g[x+lr][y] == '.' and \
        g[x][y+1] in '~#':
        x += lr
        
def drop(limy):
  global y
  while g[x][y+1] == '.' and \
        y <= limy-1:    
    y += 1  
        
coords = []
for l in f:
    c = l.split(',')
    if 'x' in c[0]:
      xr = 0 
    else:
      xr = 1
    numx = c[xr].split('=')[1]
    numy = c[1-xr].split('=')[1]
    if '.' in numx:
        be = map(int, numx.split('..'))
        for x in range(be[0],be[1]+1):
            coords.append([x,int(numy)])
    if '.' in numy:
        be = map(int, numy.split('..'))
        for y in range(be[0],be[1]+1):
            coords.append([int(numx),y])
 
for c in coords:
    if c[0]-1 < mins[0]:
        mins[0] = c[0]-1
    if c[1]-1 < mins[1]:
        mins[1] = c[1]-1
    if c[0]+1 > maxs[0]:
        maxs[0] = c[0]+1
    if c[1]+1 > maxs[1]:
        maxs[1] = c[1]+1

top = mins[1]
mins[1] = 0
print 'Searching...'
for i in range(len(coords)):
  g[coords[i][0]][coords[i][1]] = '#'
spring = [0,500]
g[spring[1]][spring[0]] = '+'
x,y = spring[1],spring[0]
limy = maxs[1]-1
lly = mins[1]
btm = True
finished = False
while not finished:
  if btm:
    btm = False
    x,y = spring[1],spring[0]
  drop(limy)  
  if y == limy:
    print 'reached the bottom. do another droplet...'
    btm = True
    g[x][y] = '|'
    continue
  else:
    if y < lly+1:
      finished = True
      break
  if g[x-1][y] == '.':
    findwaterfall(L)
  else:
    findwaterfall(R)
  if g[x][y+1] != '.':
    btm = True
    if '|' in [g[x][y+1],g[x+1][y],g[x-1][y]]:
        g[x][y] = '|'
        fillclay(R)
        fillclay(L)        
    else:
      g[x][y] = '~'
      
printclay()
