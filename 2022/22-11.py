import copy
# Chinese remainder theorem

f = open('22-11.txt').read().split('\n')

itms = []
ops = []
tst = []
ta = []
fa = []
wl = []

for l in f:
    i = l.split()
    mn = 0
    if len(i) > 0:
        if i[0] == 'Monkey':
            mn = int(i[1][:-1])
            wl.append(0)
        if i[0] == "Starting":
            itmsi = [int(x.replace(',','')) for x in i[2:]]
            itms.append(itmsi)
        if i[0] == "Operation:":
            ops.append(i[3:])
        if i[0] == "Test:":
            tst.append(int(i[3]))
        if i[1] == "true:":
            ta.append(int(i[5]))
        if i[1] == "false:":
            fa.append(int(i[5]))

itms2 = copy.deepcopy(itms)

def pr():
    for i in itms:
        print(i)

def doop(op,wl):
    op1 = op2 = 0
    if op[0] == 'old': op1 = wl
    else: op1 = int(op[0])
    if op[2] == 'old': op2 = wl
    else: op2 = int(op[2])    
    if op[1] == '+': return op1+op2
    if op[1] == '*': return op1*op2
    
done = False
mn = 0
insp = [0 for i in range(len(ta))]
itms2 = [i[:] for i in itms]
for lp1 in range(20):
  for lp in range(len(ta)):
    while len(itms[mn]) > 0:   
      insp[mn] += 1      
      i = itms[mn][0]
      mwl = (doop(ops[mn],i))//3
      if mwl%tst[mn] == 0:
        itms[ta[mn]].append(mwl)        
      else:
        itms[fa[mn]].append(mwl)
      itms[mn].pop(0)    
    mn = (mn+1)%len(ta)

print(insp)
insp.sort()
print('part 1 -',insp[-1]*insp[-2])

itms = copy.deepcopy(itms2)

bm = 1
for i in tst:  
    bm *= i
print('bm',bm)

done = False
mn = 0
insp = [0 for i in range(len(ta))]
itms2 = [i[:] for i in itms]
for lp1 in range(10000):
  for lp in range(len(ta)):
    while len(itms[mn]) > 0:   
      insp[mn] += 1      
      i = itms[mn][0]
      mwl = (doop(ops[mn],i))%bm
      if mwl%tst[mn] == 0:
        itms[ta[mn]].append(mwl)        
      else:
        itms[fa[mn]].append(mwl)
      itms[mn].pop(0)    
    mn = (mn+1)%len(ta)

print(insp)
insp.sort()
print('part 2 -',insp[-1]*insp[-2])
