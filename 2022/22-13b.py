import copy
f = open('22-13.txt').read().split('\n\n')
# like shooting fish in a barrel using 
# pythons eval function

n = '1234567890a'

def cms(ob1,ob2):
    lt = type([1,2])    
    if (type(ob1) != lt) and (type(ob2) != lt):
        if ob1 < ob2:
            return -1
        elif ob1 == ob2:    
            return 0
        else: return 1
    elif (type(ob1) == lt) and (type(ob2) == lt):
        p = 0
        while p < len(ob1) and p < len(ob2):
            d = cms(ob1[p],ob2[p])
            if d == -1:
               return -1
            if d == 1:
               return 1
            p += 1
        if p == len(ob1) and p < len(ob2):
            return -1
        elif p == len(ob2) and p < len(ob1):
            return 1
        else:
            return 0
    elif (type(ob1) != lt) and (type(ob2) == lt):
        return cms([ob1],ob2)    
    else:
        return cms(ob1,[ob2]) 

tl = 0
for ps in range(len(f)):
  p = f[ps].split()   
  if cms(eval(p[0]),eval(p[1])) < 0:    
    tl += ps+1

print('part 1 -',tl)
nf = []
for ps in range(len(f)):  
  p = f[ps].split()  
  nf.append(copy.deepcopy(p[0]))
  nf.append(copy.deepcopy(p[1]))
ct2,ct6 = 1,2
for i in nf:
    if cmp(i,'[[2]]') < 0:
        ct2 += 1
for i in nf:
    if cmp(i,'[[6]]') < 0:
        ct6 += 1
print('part 2 -',ct2*ct6)
