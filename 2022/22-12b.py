f = open('22-12.txt').read().split('\n')

# Breadth First Search, done with list
# data structure after recommendation
# much quicker

g = []
for i in range(len(f)):
  l = []
  for j in range(len(f[i])):
    if f[i][j] == 'S':
      s = (i,j)
    if f[i][j] == 'E':
      e = (i,j)
    l.append(ord(f[i][j]))
  g.append(l)

drs = [[0,1],[0,-1],[1,0],[-1,0]]
q = [((s[0],s[1]),0)]
done = False
been = []
mi = len(g)
mj = len(g[0])
g[s[0]][s[1]] = ord('a')
g[e[0]][e[1]] = ord('z')

while not done:
    (i,j),ds = q[0]
    q = q[1:]
    if (i,j) == e:
        print 'part 1 -',ds
        done = True
    if (i,j) in been:
         continue
    been.append((i,j))
    for d in drs:
       ni = i+d[0]
       nj = j+d[1]
       if 0 <= ni < mi:
         if 0 <= nj < mj:
           if g[ni][nj] <= g[i][j] + 1:
            q.append(((ni,nj),ds+1))
