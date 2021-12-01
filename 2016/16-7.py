f = open('16-7.txt').read().split('\n')

def pal(st):
    for i in range(len(st)-3):
      if (st[i] == st[i+3]) and (st[i+1] == st[i+2]):
        if st[i] != st[i+1]:
          return 1
    return 0

def lpal(st,inv):
    pls = []
    for i in range(len(st)-2):
      if (st[i] == st[i+2]) and (st[i] != st[i+1]):
        if inv:
          pls.append(st[i+1]+st[i]+st[i+1])
        else:              
          pls.append(st[i:i+3])
    return pls
    
def geto(st):
    ob,ib,o = [],[],''
    for i in st:
      if i == '[': ob.append(o)
      if i == ']': ib.append(o)
      if i not in ['[',']']: o += i
      else: o = ''
    ob.append(o)
    return [ob,ib]

ct1,ct2 = 0,0
for i in f:
    [ob,ib] = geto(i)
    if sum([pal(x) for x in ob]) != 0:
      if sum([pal(x) for x in ib]) == 0:
        ct1 += 1
    opals,ipals,gd = [],[],False    
    for i in ob:
        for p in lpal(i,False):
            opals.append(p[:])    
    for j in ib:
        for p in lpal(j,True):
            ipals.append(p[:])
    for k in opals:        
        if k in ipals:            
            gd = True            
    if gd: ct2 += 1    
print('part 1 -',ct1)
print('part 2 -',ct2)
