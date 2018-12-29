# Hardest part was decrypting the question.
# Hot spot found between ip's 18-25.  Simplified by making r[4] equal to (r[1] / 256)-1
# Unoptimised code works also, just takes 3-4 hours to execute
# No doubt further optimisations are possible - trade off between development time vs. single use execution time.
# Should work in all cases provided the basic code structure is identical

f = open('18-21.txt').read().split('\n')
r = [0] * 6
bi,ip = 0,0
insts = ['addr','addi','mulr','muli','banr','bani','borr', \
         'bori','setr','seti','gtir','gtri','gtrr','eqri','eqir','eqrr']
rs = []
found = False
    
def addr(a,b,c):
  r[c] = r[a] + r[b]
def addi(a,b,c): 
  r[c] = r[a] + b
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
def setr(a,b,c): 
  r[c] = r[a]  
def seti(a,b,c): 
  r[c] = a  
def gtir(a,b,c):
  r[c] = a > r[b]
def gtri(a,b,c):
  r[c] = r[a] > b  
def gtrr(a,b,c):
  r[c] = r[a] > r[b]    
def eqir(a,b,c):
  r[c] = a == r[b]    
def eqri(a,b,c):
  r[c] = r[a] == b    
def eqrr(a,b,c):
  r[c] = r[a] == r[b]
    
def doinst():
  global ip,found  
  ins = inst[ip][0]  
  a = inst[r[bi]][1]
  b = inst[r[bi]][2]
  c = inst[r[bi]][3]

# Optimisation of hotspot - lines 18 to 25
#18 addi [4, 1, 3] [1, 65536, 5844974L, 0, 25, 18] r[c] = r[a] + b
#19 muli [3, 256, 3] [1, 65536, 5844974L, 26, 25, 19] r[c] = r[a] * b
#20 gtrr [3, 1, 3] [1, 65536, 5844974L, 6656, 25, 20] if r[a] > r[b]: r[c] = 1 ? 0
#21 addr [3, 5, 5] [1, 65536, 5844974L, 0, 25, 21] r[c] = r[a] + r[b]
#22 addi [5, 1, 5] [1, 65536, 5844974L, 0, 25, 22] r[c] = r[a] + b
#24 addi [4, 1, 4] [1, 65536, 5844974L, 0, 25, 24] r[c] = r[a] + b
#25 seti [17, 2, 5] [1, 65536, 5844974L, 0, 26, 25] r[c] = a
# ==> this is equivalent to r[4] = int(r[1]/256)

  if ip == 18 and r[4] == 1 and r[3] == 0 and r[1] > 511:
      r[4] = int(r[1]/256)
      r[5] = 25
      ip = 25
      ins = inst[ip][0]
      a = inst[r[bi]][1]
      b = inst[r[bi]][2]
      c = inst[r[bi]][3]  
  if ins == 0:
    addr(a,b,c)  
  if ins == 1:
    addi(a,b,c) 
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
    setr(a,b,c)
  if ins == 9:
    seti(a,b,c)
  if ins == 10:
    gtir(a,b,c)
  if ins == 11:
    gtri(a,b,c)
  if ins == 12:
    gtrr(a,b,c)
  if ins == 13:
    eqri(a,b,c)
  if ins == 14:
    eqir(a,b,c)
  if ins == 15:
    eqrr(a,b,c)  
    if len(rs) == 0:
        print 'part 1 - ', r[2]        
    if r[2] in rs:
        print 'part 2 - ', rs[len(rs)-1]
        found = True
    else: rs.append(r[2])
    if len(rs) % 100 == 0:
        print 'searching :-', len(rs)
  
inst = []
bi = int(f[0].split()[1])
for l in f[1:]:
    op = map(int, l.split()[1:4])
    inst.append([insts.index(l.split()[0])] + op)
while not found:
  r[bi] = ip
  doinst()
  ip = r[bi]
  ip += 1
