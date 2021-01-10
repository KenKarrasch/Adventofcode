f = open('16-20.txt').read().split('\n')
lt = [[int(y) for y in x.split('-')] for x in f]

def comb(c):
    af,nlt = [],[]    
    for k in c:
      af.append(k[0])
      af.append(k[1])
    for m in range(len(lt)):
      if m not in af:
         nlt.append(lt[m][:])
    for k in c:
      ls = lt[k[0]] + lt[k[1]]
      nlt.append([min(ls),max(ls)])    
    return nlt

c = [0]
while len(c) > 0:
  c = []  
  fd = False
  for i in range(len(lt)):
    [li,ui] = lt[i]    
    for j in range(len(lt)):
     if i != j:
      if not fd:      
       [lj,uj] = lt[j]      
       if (ui+1 >= lj) and (li < uj):        
        c.append([i,j])
        fd = True

    i += 1    
  lt = comb(c)
  print(len(lt))
minl = 10000000000000
for r in lt:
  if r[1] < minl:
    minl = r[1]
print('part 1 -',minl+1)
print('part 2 -',len(lt)-1)
