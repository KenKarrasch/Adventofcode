f = open('18-25.txt').read().split('\n')
pts = []
for p in f:
  pts.append(map(int, p.split(',')))  
cons = [0] * len(pts)
for i in range(len(pts)):
  cons[i] = i
def in3(i,j):
  if abs(pts[i][0] - pts[j][0]) + \
     abs(pts[i][1] - pts[j][1]) + \
     abs(pts[i][2] - pts[j][2]) + \
     abs(pts[i][3] - pts[j][3]) < 4:
      return True
  return False
for i in range(len(pts)):
  for j in range(i + 1,len(pts)):
      if in3(i,j):
        name = cons[j]
        for y in range(len(pts)):
          if cons[y] == name:
            cons[y] = cons[i]      
dcons = cons[:]
for y in range(len(cons)):
  for d in range(y+1,len(dcons)):    
      if cons[y] == dcons[d]:
        dcons[d] = -1;
tcons = 0
for g in dcons:
  if g != -1:
      tcons += 1
print tcons
