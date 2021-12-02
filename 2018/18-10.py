def plot(p):
   t = []
   width = 64
  
   xaxis = 100000000
   for i in range(len(p)):
     if p[i][0] < xaxis:
       xaxis = p[i][0]
   
   yaxis = 100000000
   for i in range(len(p)):
     if p[i][1] < yaxis:
       yaxis = p[i][1]
      
   xaxis = -xaxis
   yaxis = -yaxis
   for i in range(width):
     r = ['.'] * width
     t.append(r)
   for i in p:
    if i[1]+yaxis < width and i[1]+yaxis > -1 and i[0]+xaxis < width and i[0]+xaxis > -1:
      t[i[1]+yaxis][i[0]+xaxis] = '#'
   
   for g in t[:10]:
     str = ''
     for h in g:
       str += h
     print str

def getwidth(p):
   minx = 100000000
   for i in range(len(p)):
     if p[i][0] < minx:
       minx = p[i][0]
   maxx = -10000000
   for i in range(len(p)):
     if p[i][0] > maxx:
       maxx = p[i][0]
   return maxx - minx

f = open('18-10.txt','r').read().split('\n')
p = []
v = []
for i in f:
    p.append(map(int, i.split('> velocity')[0].split('<')[1].split(',')))
    v.append(map(int, i.split('> velocity')[1].split('<')[1][:-1].split(',')))

lowest = 100000
for l in range(len(p)):
  if -p[l][0]/v[l][0] < lowest:
    lowest = -p[l][0]/v[l][0]
f = lowest

iterations = 300
found = False
thisone = False
b = 10000000
for c in range(len(v)):
  p[c][0] = p[c][0] + f*v[c][0]
  p[c][1] = p[c][1] + f*v[c][1]
for i in range(iterations):
  for c in range(len(v)):
     p[c][0] = p[c][0] + v[c][0]
     p[c][1] = p[c][1] + v[c][1]
  prev = b
  b = getwidth(p)
  if prev < b:
    for c in range(len(v)):
      p[c][0] = p[c][0] - v[c][0]
      p[c][1] = p[c][1] - v[c][1]
    if not found:
      print 'part 1 -'
      plot(p)
      print 'part 2 -', f + i
    found = True  
 
