with open('19-19.txt') as fp: pr = { i: int(x) for i, x in enumerate(fp.readline().split(',')) }

# Nice easy one


def cmd(x,y):
  global pr
  p = dict(pr)
  pc,rb,inp = 0,0, [x,y]
  while True:
    (m, c), a = divmod(p[pc], 100), []
    for (i,iswrite) in enumerate([[],[0,0,1],[0,0,1],[1],[0],[0,0],[0,0],[0,0,1],[0,0,1],[0]][c%99]):
      a += [p[pc+i+1]]
      if m % 10 == 2: a[-1] += rb
      if m % 10 != 1 and iswrite == 0: a[-1] = p.get(a[-1],0)
      m //= 10
    og = pc
    if c == 1: p[a[2]] = a[0] + a[1] # add
    elif c == 2: p[a[2]] = a[0] * a[1] # multiply
    elif c == 3: p[a[0]] = inp.pop(0) # input
    elif c == 4: #output
      return a[0]
    elif c == 5 and a[0] != 0: pc = a[1] # branch if true
    elif c == 6 and a[0] == 0: pc = a[1] # branch if false
    elif c == 7: p[a[2]] = int(a[0] < a[1]) # test less than
    elif c == 8: p[a[2]] = int(a[0] == a[1]) # test equal
    elif c == 9: rb += a[0] # adjust relative base
    elif c == 99: break # halt
    if pc == og: pc += len(a) + 1 #only go to the next instruction if we didn't jump

sz,tly = 50,0
for x in range(sz):
    for y in range(sz):
        if cmd(x,y): tly += 1
print('part 1 -',tly)
x,y,fd = 5,5,False
fd = False
while not fd:
    y += 1
    while not (cmd(x,y) == 1): x += 1      
    if (cmd(x+99,y-99) == 1):           
       print ('part 2 -',x*10000+(y-99))
       fd = True
