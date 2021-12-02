r = [u.split(')') for u in open('19-6.txt').read().split('\n')]

book, sanp,youp = [],[],[]

def exp(r,d,p):
  p.append(book[r][0])
  sanp, youp, you, san = [],[],[],[]
  if len(book[r]) == 1:
      if book[r][0] == 'SAN': sanp = p[:]
      if book[r][0] == 'YOU': youp = p[:]
      return d,sanp,youp
  ty = d
  for y in book[r][1:]:
    tly,san,you = exp(y[1],d+1,p[:])
    if len(san) != 0: sanp = san[:]
    if len(you) != 0: youp = you[:]
    ty += tly
  return ty,sanp,youp
    
st = 0

for t in r:
  u = [t[1]]
  for y in range(len(r)):
    if r[y][0] == t[1]:
      u.append([r[y][1],y])
  book.append(u)

for h in range(len(r)):
    if r[h][0] == 'COM':
        st = h
        
ds,sanp,youp = exp(st,1,[])
print 'part 1 -',ds
it = min([len(sanp),len(youp)])
for e in range(it):
    if youp[e] != sanp[e]:
       print 'part 2 -',(len(sanp)+len(youp)-2*e)-1
       break
