f = [i.split('-') for i in open('21-12test2.txt').read().split('\n')]
# pt2 - Took a while working out what was meant by 'single small cave' but finally figured out that only one small cave can visited twice.
g = [i[:] for i in f]
for h in g: f.append([h[1],h[0]])
tks,pl,sm = [0 for i in f],[],{}
for i in f:
    if i[0] not in pl: pl.append(i[0])
for i in pl:
    if i[0] in 'qwertyuiopasdfghjklzxcvbnm': sm[i] = 0
    if i[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM': sm[i] = -100000        

def mv(op,fsm,depth,path,pt):      
    if depth == 2 and pt == 2:
        print('searching', path)    
    if list(fsm.values()).count(2) > 1: return 0         
    if op == 'end': return 1
    if op == 'start' and depth != 0: return 0
    tkc = 0        
    for i in range(len(f)):  
        if f[i][0] == op:
            if fsm[f[i][0]] < pt:                
                nsm = fsm.copy()
                nsm[f[i][0]] += 1                             
                tkc += mv(f[i][1],nsm,depth+1,path+','+f[i][1],pt) 
    return tkc

pos = 'start'
print('part 1 -',mv(pos,sm,0,'start',1))
print('part 2 -',mv(pos,sm,0,'start',2))
