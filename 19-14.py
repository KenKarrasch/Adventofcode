import re

import collections

with open('19-14.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    lines = [[i for i in re.findall(r'-?\d+|[A-Z]+', l)] for l in lines]
# needed help for part 1. Still not convinced it would for all cases.
# part 2 was straightforward binary search.

    outs = {}
    
    for line in lines:
        co, cq = line[-2:]
        co = int(co)

        ins = []
        for a, b in zip(line[:-2][::2], line[:-2][1::2]):
            ins.append((int(a), b))
        outs[cq] = (co, ins)
    
def fdore(num):
        
    #for a in outs: print a,outs[a]
    need = {'FUEL':num}
    have = collections.defaultdict(int)
    while True:
        
      try:
        nk = next(n for n in need if n != 'ORE')
        #print nk
      except StopIteration:
                break
      
      quant, ins = outs[nk]
      #print 'q,ins,neednk,nk',quant,ins,need[nk],nk
      # amt needed / quantities available
      d , m = divmod(need[nk], quant)
      #print 'd,m',d,m
      if m == 0:
        del need[nk] # just the right amount
      else:
        del need[nk]
        have[nk] = quant - m #amt needed - just bought = left over
        d += 1 # add one more to cover the need
      #print 'ins',ins
      for a, b in ins:
        #print 'abneed',a,b,need
        # add new ingredients to need list, take away any previous leftovers
        need[b] = need.get(b, 0) + d * a - have[b]
        del have[b]
    return need['ORE']

done = False 
print 'part 1 -',fdore(1)
oreav = 1000000000000
f = 4
pf = 2
mx = 0
while mx == 0:
    o = fdore(int(f))
    if o < oreav:
       pf = f
       f *= 2
    else:
        mx = f
f = mx
while not done:
    m = int((pf + f)/2)
    op = o
    o = fdore(int(m))
    print o,pf,m,f
    if m == pf:
         print o, f
         print fdore(m-1),m-1
         print fdore(m),m
         print fdore(m+1),m+1
         done = True
    if o < oreav:
       pf = m
    else:
       f = m
