f = open('16-8.txt').read().split('\n')
xsz,ysz = 50,6
gr = [['.' for x in range(xsz)] for y in range(ysz)]

def pgr(gr):
    l = ''
    for i in gr:
      print(l.join(i))

for l in f:
    if 'rect' in l:
      [x,y] = [int(x) for x in l.split()[1].split('x')]      
      for i in range(x):
        for j in range(y):
          gr[j][i] = '#'
    if ('x=' in l) or ('y=' in l):
      ln = int(l.split()[2][2:])
      md = int(l.split()[4])
      st = []
      if 'x=' in l:
        for i in range(ysz):
          st.append(gr[i][ln])      
        for i in range(ysz):
          gr[(i+md)%ysz][ln] = st[i]
      if 'y=' in l:
        for i in range(xsz):
          st.append(gr[ln][i])      
        for i in range(xsz):
          gr[ln][(i+md)%xsz] = st[i]    
ct = 0
for x in gr:
  for y in x:
    if y == '#':
      ct += 1          
print('part 1 -',ct)
print('part 2 -')
pgr(gr)
