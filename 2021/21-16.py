f = open('21-16.txt').read()
# Stuggled with this one, took a while to get the buffering right
# Had all the samples right, but not the real input. Hard to debug
buf = 0
fs = bin(int(f, 16))[2:]
pfx = 0
for bf in f:
        if bf != '0':
            break    
        pfx += 1
mp = [0,3,2,1] 
buf = mp[len(fs)%4] + (4*pfx)
pr = ''
for i in range(buf):
    pr += '0'
rd = pr + fs
ptrg = 0
otl = [0]

def parse(b,ptr,depth,it):       
  while it > 0:
    it -= 1
    v = int(b[ptr:ptr+3],2)
    ti = int(b[ptr+3:ptr+6],2)
    msg = ''    
    otl[0] += v
    vl = 0
    if ti == 4:        
        u = 6 + ptr
        dn = False
        while not dn:            
            st = b[u+1:u+5]
            msg += st
            if b[u] == '0': 
                dn = True
            u += 5
        ptr = u 
        vl = int(msg,2)
    else:        
        vls = []
        u = 6 + ptr
        lt = b[u]
        if lt == '0':
            u = 7 + ptr
            l = int(b[u:u+15],2)            
            u += 4+11            
            endp = u + l
            ptr = u
            while ptr < endp:                
                nvl, nptr = parse(b[u:u+l],0,depth+1,1)  
                u += nptr
                ptr += nptr                
                vls.append(nvl)
        if lt == '1':        
            u = 7 + ptr            
            sp = int(b[u:u+11],2)                        
            u += 11            
            for i in range(sp):                
                ss = b[u:]
                nvl, nptr = parse(ss,0,depth+1,1)                   
                u += nptr
                vls.append(nvl)                
                ptr = u            
        if ti == 0: vl = sum(vls)
        if ti == 1: 
            vl = 1
            for i in vls: vl *= i
        if ti == 2: vl = min(vls)
        if ti == 3: vl = max(vls)
        if ti == 5:             
            if vls[0] > vls[1]: vl = 1
            else: vl = 0
        if ti == 6: 
            if vls[0] < vls[1]: vl = 1
            else: vl = 0
        if ti == 7: 
            if vls[0] == vls[1]: vl = 1
            else: vl = 0
  return vl,ptr

ans = parse(rd,ptrg,0,1)[0]
print('part 1 -',otl[0])
print('part 2 -',ans)
