f = open('18-1.txt','r')
s = f.read()
b = s.split('\n')
sh = 0
l = []
db = [0 for i in range(300000)]
fd = False

for y in range(200):
  for t in b:
    if t[0] == '+':
        si = 1
    if t[0] == '-':
        si = -1
    sh = sh + int(t[1:])*si
    
    if db[sh] == 1:
      if fd== False:
        print 'part 2 - ', sh
        fd = True
    db[sh] = 1
  if y == 0:
    print 'part 1 - ', sh
