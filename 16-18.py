f = open('16-18.txt').read()

sz = len(f)
print(sz)
its = 400000
ln = ['.' for x in range(sz)]

traps = [['^','^','.'],\
         ['.','^','^'],\
         ['^','.','.'],\
         ['.','.','^']]

ct = sz 
for i in range(len(f)):
  if f[i] == '^':
    ln[i] = '^'
    ct -= 1

y = 0
sti = ''
print(sti.join(ln))
while y < its-1:  
  nl = ln[:]
  for x in range(sz):    
    ts = []
    for sc in [-1,0,1]:      
      if sz > x+sc >= 0:        
        ts.append(ln[x+sc])
      else:
        ts.append('.')    
    if ts in traps:        
      nl[x] = '^'      
    else:
      nl[x] = '.'
      ct += 1
  ln = nl[:]
  y += 1
  sti = ''  
  if y%10000==0:
    print(y, 'of 400,000')
print('part 1 -',ct)
      f = open('16-18.txt').read()

sz = len(f)
print(sz)
its = 400000
ln = ['.' for x in range(sz)]

traps = [['^','^','.'],\
         ['.','^','^'],\
         ['^','.','.'],\
         ['.','.','^']]

ct = sz 
for i in range(len(f)):
  if f[i] == '^':
    ln[i] = '^'
    ct -= 1

y = 0
sti = ''
print(sti.join(ln))
while y < its-1:  
  nl = ln[:]
  for x in range(sz):    
    ts = []
    for sc in [-1,0,1]:      
      if sz > x+sc >= 0:        
        ts.append(ln[x+sc])
      else:
        ts.append('.')    
    if ts in traps:        
      nl[x] = '^'      
    else:
      nl[x] = '.'
      ct += 1
  ln = nl[:]
  y += 1
  sti = ''  
  if y%10000==0:
    print(y, 'of 400,000')
print('part 1 -',ct)
      
