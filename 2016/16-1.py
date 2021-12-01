f = open('16-1.txt').read().split(', ')
m = [[0,1],[1,0],[0,-1],[-1,0]]
x,y,p,d = 0,0,0,0
ls,fd = [],False
for i in f:
    p = int(i[1:])
    if 'R' in i: d = (d+1)%4
    else: d = (4+d-1)%4
    for j in range(p):
      x += m[d][0]
      y += m[d][1]
      if [x,y] in ls:
       if not fd:
        fd = True
        print 'part 2-',abs(x)+abs(y)
      ls.append([x,y])
print 'part 1-', abs(x)+abs(y)
