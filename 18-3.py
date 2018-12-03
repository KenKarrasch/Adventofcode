f = open('18-3.txt','r')
b = f.read().split('\n')
db = [[0 for i in range(1000)] for j in range(1000)]
ct = 0
for e in b:
   elf = e.split(' ')
   t = [int(n) for n in elf[2][:-1].split(',')]
   s = elf[3].split('x')
   for x in range(int(s[0])):
    for y in range(int(s[1])):
      db[t[0]+x][t[1]+y] = db[t[0]+x][t[1]+y] + 1
for x in range(1000):
  for y in range(1000):
     if db[x][y] > 1:
         ct = ct + 1
print 'part 1 -', ct

for e in b:
   dud = False
   elf = e.split(' ')
   t = elf[2][:-1].split(',')
   s = elf[3].split('x')
   for x in range(int(s[0])):
    for y in range(int(s[1])):
       if db[int(t[0])+x][int(t[1])+y] != 1:
        dud = True
   if dud == False:
       print 'part 2 -', e.split(' ')[0][1:]
 
