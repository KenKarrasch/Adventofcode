r = open('21-4.txt').read().split('\n')
#Let the Squid win, or else
n = [int(j) for j in r[0].split(',')]
sz = int((len(r)-1)/6)
wm,scs,ss = [],[],[]

for s in range(sz):
    sht = []
    for k in [0,1,2,3,4]:    
        i = r[2+k+s*6]
        sht.append([int(j) for j in i.split()])       
    ss.append([j for j in sht[:]])

def getsc(sd,n,sn):
    tly = 0
    for j in [0,1,2,3,4]:    
        for i in [0,1,2,3,4]:
            if sd[i][j] != -1:
                tly += sd[i][j]     
    if sn not in wm:
        scs.append(tly*n)
        wm.append(sn)

def wn(n):
    for shts in range(len(ss)):                
        for i in [0,1,2,3,4]:            
            e = True
            for j in [0,1,2,3,4]:
                if ss[shts][i][j] != -1:                     
                    e = False
            if e: getsc(ss[shts],n,shts)                                  
        for j in [0,1,2,3,4]:    
            e = True        
            for i in [0,1,2,3,4]:
                if ss[shts][i][j] != -1:                     
                    e = False
            if e: getsc(ss[shts],n,shts)                
    return(False)

for ns in n:
    for shts in ss:
        for i in [0,1,2,3,4]:
            for j in [0,1,2,3,4]:                
                if shts[i][j] == ns:                 
                    shts[i][j] = -1    
    wn(ns)
print('part 1 -',scs[0])
print('part 2 -',scs[len(scs)-1])
