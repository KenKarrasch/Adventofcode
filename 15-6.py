import re
f = open('15-6.txt').read().split('\n')
sz,w = 1000,[0,1]
g = [[[0 for i in range(sz)] for i in range(sz)] for z in w]
p = ['part 1 - ','part 2 - ']
for a in f:
  sq = [int(v) for v in re.findall("[0-9]+", a)]
  d = 2
  if 'off' in a: d = -1
  if 'on' in a: d = 1
  for x in range(sq[0],sq[2]+1):
    for y in range(sq[1],sq[3]+1):
      if d == 2: g[0][x][y] = not g[0][x][y]
      if d == 1: g[0][x][y] = 1
      if d == -1: g[0][x][y] = 0
      g[1][x][y] += d
      if g[1][x][y] < 0: g[1][x][y] = 0
      
print [p[k] + str(sum([sum(y) for y in g[k]])) for k in range(len(g))]
