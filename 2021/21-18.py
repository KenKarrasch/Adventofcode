import copy
import itertools

# Parse straight into python list data structure, then do the explosions, 
# then splitting (vice versa), then sum up recursively.
# Need to keep track of numbers are to distribute explosions.
# for part 2, use permutation function from itertools to compare each pair

f = open('21-18.txt').read().split('\n')

def get(st,depth):
    chn,sti = 0,[]
    sti = []   
    while chn < len(st):
        i = st[chn]          
        if i == '[':
            cn, ob = get(st[chn+1:],depth+1)
            sti.append(ob)
            chn += cn
        elif i == ']': return chn+1,sti
        else:
            if i in '01234567890':
                n = int(i)
                sti.append(n)               
        chn += 1        
    return len(st), sti

bk = []
for i in f:
    pg = []
    for ch in i:    
        if ch != ',':
            pg.append(ch)    
    bk.append(pg[:])

bkc = []
for i in bk:
   bkc.append(get(i,0)[1][0])

busy = True
edone = [False]
fns,sns,exn,tn = [0],[0],[0],[0]

def explodefn(nls,depth):         
    if type(nls) is int:         
        exn[0] += 1    
        if exn[0] == tn[0]:
            return nls+fns[0], False
        if exn[0] == tn[0]+2:
            return nls+sns[0], False            
        return nls, False
    ls = copy.deepcopy(nls)
    nnls = []
    chn = False    
    for i in ls:                    
        nlst, changed = explodefn(i,depth + 1)        
        nnls.append(nlst)
        if changed: chn = True
    return nnls, chn


def explode(nls,depth):     
    if type(nls) is int:    
        exn[0] += 1                  
        return nls, False
    ls = copy.deepcopy(nls)
    if depth == 4 and not edone[0]:       
        for i in ls:
            if type(i) is int: exn[0] += 1  
            else: tn[0] = exn[0]     
        fp = -1        
        for i in range(len(ls)):            
            if type(ls[i]) is not int:                        
                if fp == -1:
                    fp = i        
        if fp == -1: # no pairs           
            return ls, False
        else:         
            edone[0] = True   
            fn = ls[fp][0]
            sn = ls[fp][1]
            ls[fp] = 0            
            fns[0] = fn  
            sns[0] = sn              
            if fp == len(ls)-1:                 
                return ls, True
            return ls, True
    nnls = []
    chn = False    
    for i in ls:         
        nlst, changed = explode(i,depth + 1)        
        nnls.append(nlst)
        if changed: chn = True
    return nnls, chn

def splitn(nls,depth):         
    if type(nls) is int:           
        if nls > 9 and not edone[0]: 
            edone[0] = True           
            fn = sn = nls//2
            if fn + sn < nls:
                sn += 1
            return [fn,sn],True        
        return nls, False
    ls = copy.deepcopy(nls)
    nnls = []
    chn = False    
    for i in ls:
        nlst, changed = splitn(i,depth + 1)        
        nnls.append(nlst)
        if changed: chn = True
    return nnls, chn

action = 'explode'
ex1 = bkc[0]
for nextone in bkc[1:]:
   ex1 = [ex1,nextone]   
   action = 'explode' 
   print(ex1)
   while action != 'done':    
    edone[0] = False
    if action == 'explode':   
        fns[0],sns[0],tn[0],exn[0] = -1,-1,-1,0
        nl, changed = explode(ex1,1)                  
        ex1 = copy.deepcopy(nl)           
        if changed: 
            action = 'explode'           
            exn[0] = 0               
            nl, changed = explodefn(ex1,1)  
        else:  action = 'split'                                
    else:        
        nl, changed = splitn(ex1,0)
        if changed: action = 'explode'
        else:
            action = 'done'    
    ex1 = copy.deepcopy(nl)   

def getv(ls): 
    if type(ls) is int: return ls
    m,vl = 3,0    
    for i in ls:
        vl += m*getv(i)
        m -= 1
    return vl

print('part 1 -',getv(ex1))
perms = [list(i) for i in itertools.permutations(range(len(bkc)),2)]
prs = []
for it in perms:
   ex1 = [bkc[it[0]],bkc[it[1]]]
   action = 'explode'
   while action != 'done':    
    edone[0] = False
    if action == 'explode':   
        fns[0],sns[0],tn[0],exn[0] = -1,-1,-1,0
        nl, changed = explode(ex1,1)                  
        ex1 = copy.deepcopy(nl)   
        if changed: 
            action = 'explode'           
            exn[0] = 0               
            nl, changed = explodefn(ex1,1)  
        else:  action = 'split'                                
    else:        
        nl, changed = splitn(ex1,0)
        if changed: action = 'explode'
        else:
            action = 'done'    
    ex1 = copy.deepcopy(nl)  
   prs.append(getv(ex1))
   
print('part 2 -',max(prs))
