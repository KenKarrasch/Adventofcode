fn,f = [i.split() for i in open("17-8.txt").read().split('\n')],[]
op,mx,reg = [],0,{}

def do(v,op,n):
    if op == 'dec': return reg[v]-n
    return reg[v]+n

for i in fn:
    if i[0] not in reg: reg[i[0]] = 0
for i in fn:
    ninst = []
    for j in range(len(i)):
        if j == 2 or j == 6: ninst.append(int(i[j]))
        else: ninst.append(i[j])
    f.append(ninst)
for j in f:    
    d = False
    if j[5] == '>' and reg[j[4]] > j[6]: d = True
    if j[5] == '<' and reg[j[4]] < j[6]: d = True
    if j[5] == '>=' and reg[j[4]] >= j[6]: d = True
    if j[5] == '==' and reg[j[4]] == j[6]: d = True
    if j[5] == '<=' and reg[j[4]] <= j[6]: d = True
    if j[5] == '!=' and reg[j[4]] != j[6]: d = True  
    if d: reg[j[0]] = do(j[0],j[1],j[2])    
    bt = reg.values()
    if mx < max(bt): mx = max(bt)
bt = reg.values()
print('part 1 -',max(bt))
print('part 2 -',mx)
