import copy

s = open('15-18.txt').read().split('\n')

grid = []
for i in s:
  grid.append([x for x in i])

def cth(gr):
  ct = 0
  for i in range(lx):
    for j in range(ly):
      if gr[i][j] == '#':
         ct += 1
  return ct

lx = len(grid[0])
ly = len(grid)

def dogr(gr,ln,pt):
  for i in range(ln):
    ngrid = [['.' for x in range(lx)] for y in range(ly)]
    if pt == 2:
      gr[0][0] = '#'
      gr[0][ly-1] = '#'
      gr[lx-1][0] = '#'
      gr[lx-1][ly-1] = '#'    
    for i in range(lx):
      for j in range(ly):
        ct = 0
        for x in [-1,0,1]:
          for y in [-1,0,1]:
            if lx > i+x >= 0:
              if ly > j+y >= 0:
                if [x,y] != [0,0]:
                  if gr[i+x][j+y] == '#':
                    ct += 1        
        if gr[i][j] == '#':
          if ct in [2,3]: ngrid[i][j] = '#'            
          else: ngrid[i][j] = '.'
        if gr[i][j] == '.':
          if ct in [3]: ngrid[i][j] = '#'
          else: ngrid[i][j]= '.'
    gr = copy.deepcopy(ngrid)
  return gr

print('part 1 -',cth(dogr(grid,100,1)))
grid = dogr(grid,100,2)
grid[0][0] = '#'
grid[0][ly-1] = '#'
grid[lx-1][0] = '#'
grid[lx-1][ly-1] = '#'
print('part 2 -',cth(grid))
