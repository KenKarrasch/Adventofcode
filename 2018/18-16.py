f = open('18-16.txt').read().split('\n')

def solved(opcode):
  count = 0
  for i in opcode:
    for j in i:
      if j == 1:
        count += 1
  if count == 16:
    return True
  else:
    return False

def addr(a,b,c,r):  
  r[c] = r[a] + r[b]  

def addi(a,b,c,r):
  r[c] = r[a] + b

def mulr(a,b,c,r):
  r[c] = r[a] * r[b]

def muli(a,b,c,r):
  r[c] = r[a] * b

def banr(a,b,c,r):
  r[c] = r[a] & r[b]
  
def bani(a,b,c,r):
  r[c] = r[a] & b
  
def borr(a,b,c,r):
  r[c] = r[a] | r[b]
  
def bori(a,b,c,r):
  r[c] = r[a] | b

def setr(a,b,c,r):
  r[c] = r[a]

def seti(a,b,c,r):
  r[c] = a

def gtir(a,b,c,r):
  if a > r[b]:
    r[c] = 1
  else: r[c] = 0

def gtri(a,b,c,r):
  if r[a] > b:
    r[c] = 1
  else: r[c] = 0

def gtrr(a,b,c,r):
  if r[a] > r[b]:
    r[c] = 1
  else: r[c] = 0

def eqir(a,b,c,r):
  if a == r[b]:
    r[c] = 1
  else: r[c] = 0

def eqri(a,b,c,r):
  if r[a] == b:
    r[c] = 1
  else: r[c] = 0

def eqrr(a,b,c,r):
  if r[a] == r[b]:
    r[c] = 1
  else: r[c] = 0


def doinst(it,reg,optor):
  if optor[it[0]] == 0:
    addr(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 1:
    addi(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 2:
    mulr(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 3:
    muli(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 4:
    banr(it[1],it[2],it[3],reg)
  if optor[it[0]] == 5:
    bani(it[1],it[2],it[3],reg)
  if optor[it[0]] == 6:
    borr(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 7:
    bori(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 8:
    setr(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 9:
    seti(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 10:
    gtir(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 11:
    gtri(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 12:
    gtrr(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 13:
    eqir(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 14:
    eqri(it[1],it[2],it[3],reg)  
  if optor[it[0]] == 15:
    eqrr(it[1],it[2],it[3],reg)  
  
bef = []
aft = []
r = []
reg = []
inst = []

  
inst = []

for l in f:  
  if 'Before' in l:
    bef.append(map(int, l.split('[')[1].split(']')[0].split(',')))
  if 'After' in l:
    aft.append(map(int, l.split('[')[1].split(']')[0].split(',')))
  if not '[' in l and len(l) > 0:
    r.append(map(int, l.split()) )

opcode = [[1 for i in range(16)] for v in range(16)]
    
inst = r[:len(aft)]
total = 0
for s in range(len(bef)):
    count = 0
    
    reg = bef[s][:]
    addr(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][0] = 0
      

    reg = bef[s][:]
    addi(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][1] = 0
      
    reg = bef[s][:]
    mulr(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][2] = 0
      
    reg = bef[s][:]
    muli(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][3] = 0

    reg = bef[s][:]
    banr(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][4] = 0  

    reg = bef[s][:]
    bani(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][5] = 0  
      
    reg = bef[s][:]
    borr(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][6] = 0  
      
    reg = bef[s][:]
    bori(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][7] = 0  
            
    reg = bef[s][:]
    setr(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][8] = 0  
      
    reg = bef[s][:]
    seti(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][9] = 0  
      
    reg = bef[s][:]
    gtir(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][10] = 0  
      
    reg = bef[s][:]
    gtri(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][11] = 0  
      
    reg = bef[s][:]
    gtrr(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][12] = 0  

    reg = bef[s][:]  
    eqir(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][13] = 0  
            
    reg = bef[s][:]
    eqri(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][14] = 0  

    reg = bef[s][:]
    eqrr(inst[s][1],inst[s][2],inst[s][3],reg)
    if reg == aft[s]:
      count += 1
    else:
      opcode[inst[s][0]][15] = 0  

    if count > 2:
      total += 1


print 'part 1 -', total

wipe = -1


h = 0
while not solved(opcode):
 for h in range(16):
  count = 0  
  for j in range(16):
    if opcode[h][j] == 1:
      count += 1
      wiperule = j
      goodrule = h
  newopcodes = []
  if count == 1:    
    for opcodenum in range(16):
      nopcode = []
      for rule in range(16):
        if rule == wiperule and not goodrule == opcodenum:                    
          nopcode.append(0)
        else:
          nopcode.append(opcode[opcodenum][rule])
      newopcodes.append(nopcode)    
    for i in range(16):    
     for j in range(16):
      opcode[i][j] = newopcodes[i][j]

optor = [] # [opcode][rule]
for i in range(16):    
  for j in range(16):
    if opcode[i][j] == 1:
      optor.append(j)

reg = [0,0,0,0]

for instr in r[len(bef):]:
  doinst(instr,reg,optor)

print 'part 2 -', reg[0]
