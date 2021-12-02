f = open('20-3.txt').read().split('\n')
# 13 mins - straightforward one

x,y,t,m = 0,0,0,1
w = len(f[0])
for l in range(len(f)):
    if f[y][x%w] == '#':
        t += 1
    x += 3
    y += 1
print 'part 1 -',t
for g in [1,3,5,7]:
  x,y,t = 0,0,0
  for l in range(len(f)):
    if f[y][x%w] == '#':
        t += 1
    x += g
    y += 1
  m *= t
x,y,t = 0,0,0
for l in range(len(f)):
    if y < len(f):
     if f[y][x%w] == '#':
        t += 1
    x += 1
    y += 2
m *= t
print 'part 2 -',m
