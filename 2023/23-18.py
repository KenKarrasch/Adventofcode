f = open('23-18.txt').read().split('\n')

# invented a triangle summing algorithm, then added the border

dr = {'R': [-1,0],'L':[1,0],'U':[0,1],'D':[0,-1]}

pdict = ['R','D','L','U']

for part in [1,2]:
  a = 0
  p = [0,0]
  ds = []
  for i in f:
    if part == 2:
      dc = i.split()[2][2:-1]
      pt = pdict[int(dc[-1])]
      ln = ''
      for i in dc[:-1]:
        ln += i
      d = int(ln,16)
    else:
        pt = i.split()[0]
        dc = i.split()[1]
        d = int(dc)
    ds.append(d)
    dx = dr[pt][0]*d
    dy = dr[pt][1]*d
    
    pb = p[:]
    p[0] += dx
    p[1] += dy
    
    a += (pb[0]+p[0])*(pb[1]-p[1])

  print 'part', part,1+abs((a/2)) + (sum(ds)/2)
