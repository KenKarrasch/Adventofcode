import copy
cd = int(open('16-13.txt').read())
sz = 100
gr = [['.' for i in range(sz)] for j in range(sz)]

for x in range(sz):
  for y in range(sz):
    n = x*x + 3*x + 2*x*y + y + y*y + cd
    if sum([int(b) for b in bin(n)[2:]])%2 == 1:
      gr[y][x] = '#'
fd,d,dest = False,0,[39,31]
gr[1][1] = '0'
while not fd:
  ngr = copy.deepcopy(gr)
  for x in range(sz):
   for y in range(sz):
    if gr[x][y] == str(d%10):
      for xs,ys in [[-1,0],[1,0],[0,1],[0,-1]]:
          if 0 <= x+xs < sz:
            if 0 <= y+ys < sz:
              if gr[x+xs][y+ys] == '.':
                ngr[x+xs][y+ys] = str((d+1)%10)
                if [x+xs,y+ys] == dest:
                  print('part 1 -',d+1)                  
                  fd = True
                  break
  gr = copy.deepcopy(ngr)
  if d == 50:
      ct = 0
      for x in range(sz):
       for y in range(sz):
         if gr[x][y] not in '#.':
           ct += 1
      print('part 2 -',ct-1)
  d += 1
