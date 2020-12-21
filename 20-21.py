import copy

f = open('20-21.txt').read().split('\n')

# Logical reasoning puzzle

t,ingr,aler,aldef = [],[],[],[]

for i in f:
    its = []
    pt =  i.split('(')
    for it in pt[0].split():
        its.append(it)
    ingr.append(its)
    al = pt[1][8:-1].split(',')
    al = [i.replace(' ','') for i in al]
    t.append(al[:])

for i in t:
    for j in i:
        if j not in aler:            
            aler.append(j)

def setunion(s1,s2):
    su = []
    for i in s1:
        if i in s2:
            su.append(i)
    return(su)

aldef = []
for al in range(len(aler)):   # For each alergen
    first = True
    alu = []
    for tox in range(len(t)): # search through each ingredient list
        als = []
        if aler[al] in t[tox]:
            for i in ingr[tox]:
                als.append(i)
            if first:
                alu = als[:]
                first = False
            else:
                alu = setunion(alu,als)
    aldef.append(alu)

done = False
while not done:
  i = 0
  while i < len(aldef):
    if len(aldef[i]) == 1:
        naldef = []
        for x in range(len(aldef)):
            nl = []
            for y in range(len(aldef[x])):
                if (aldef[x][y] != aldef[i][0]) or (x == i):                    
                    nl.append(aldef[x][y])
            naldef.append(nl)
        aldef = copy.deepcopy(naldef)
    i += 1
    ct = 0
    for u in aldef: ct += len(u)
    if len(aler) == ct: done = True
ct = 0
for i in ingr:
    for j in i:
        if [j] not in aldef:
          ct += 1
print('part 1 -',ct)
saler,stri = [],''
for f in range(len(aler)):
    saler.append([aler[f],f,aldef[f][0]])
saler.sort()
for i in saler:    
    stri = stri + ',' + i[2]
print('part 2 -',stri[1:])
