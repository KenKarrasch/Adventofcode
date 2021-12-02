f = open('18-19.txt').read().split('\n')
# Trick for part 2 - compute the starting number, this is register 4 when registers 0-3 are zero. (this happens after about 10-15 iterations). Answer is simply the addition of all factors of the number.
# (working this out was hard won, a few hours sifting through the results, writing test cases spotting patterns, etc)
# As a benchmark, if simply executing to completion, part 2 will take about 1 billion times as long as part 1, about 200 yrs on my phone.
# This solution should work in all cases, provided the basic structure of input is the same.
r = [0,0,0,0,0,0]
bi = 0
ip = 0

def cf(x):
    factors = 0
    fct = []
    if x >= 1:
        for y in range(1,x+1):
            if not ( x % y ):
                factors += 1
                fct.append(y)
    print 'part 2 -', sum(fct)
    
def addr(a,b,c,bi):  #
  global ip
  r[c] = r[a] + r[b]
  ip = r[bi]

def addi(a,b,c,bi): #
  global ip
  r[a] += b
  ip = r[bi]

def mulr(a,b,c):
  r[c] = r[a] * r[b]

def muli(a,b,c):
  r[c] = r[a] * b

def banr(a,b,c):
  r[c] = r[a] & r[b]
  
def bani(a,b,c):
  r[c] = r[a] & b
  
def borr(a,b,c):
  r[c] = r[a] | r[b]
  
def bori(a,b,c):
  r[c] = r[a] | b

def setr(a,b,c,bi): #
  global ip
  r[c] = r[a]
  ip = r[bi]

def seti(a,b,c,bi): #
  global ip
  r[c] = a
  ip = r[bi]
  
def gtir(a,b,c):
  if a > r[b]:
    r[c] = 1
  else: r[c] = 0

def gtri(a,b,c):
  if r[a] > b:
    r[c] = 1
  else: r[c] = 0

def gtrr(a,b,c):
  if r[a] > r[b]:
    r[c] = 1
  else: r[c] = 0

def eqir(a,b,c):
  if a == r[b]:
    r[c] = 1
  else: r[c] = 0

def eqri(a,b,c):
  if r[a] == b:
    r[c] = 1
  else: r[c] = 0

def eqrr(a,b,c):
  if r[a] == r[b]:
    r[c] = 1
  else: r[c] = 0

def doinst():
  global bi
  global ip
  
  r[bi] = ip
  ins = inst[ip][0]
  a = inst[r[bi]][1]
  b = inst[r[bi]][2]
  c = inst[r[bi]][3]
  if ins == 0:
    addr(a,b,c,bi)  
  if ins == 1:
    addi(a,b,c,bi) 
  if ins == 2:
    mulr(a,b,c) 
  if ins == 3:
    muli(a,b,c) 
  if ins == 4:
    banr(a,b,c)
  if ins == 5:
    bani(a,b,c)
  if ins == 6:
    borr(a,b,c)
  if ins == 7:
    bori(a,b,c)
  if ins == 8:
    setr(a,b,c,bi)
  if ins == 9:
    seti(a,b,c,bi)
  if ins == 10:
    gtir(a,b,c)
  if ins == 11:
    gtri(a,b,c)
  if ins == 12:
    gtrr(a,b,c)
  if ins == 13:
    eqir(a,b,c)
  if ins == 14:
    eqri(a,b,c)
  if ins == 15:
    eqrr(a,b,c)
  r[bi] = ip
  
def instnum(istr):
  i = ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']
  for u in range(len(i)):
    if i[u] in istr:
      return u
  return -1
  
inst = []

bi = int(f[0].split()[1])
for l in f[1:]:
    instn = instnum(l.split()[0])
    op = map(int, l.split()[1:4])
    inst.append([instn] + op)
cpy = r[:]
for i in range(2):
 r = cpy[:]
 r[0] = i
 done = False
 while ip < len(inst) and not done:
  doinst()
  if i == 1:
    if [0,0,0,0] == r[:4]:
      cf(r[4])
      done = True
  ip = r[bi] + 1
 ip = 0
 if i == 0:
   print 'part 1 -', r[0]
