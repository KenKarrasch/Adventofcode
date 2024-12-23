f = [i.split('-') for i in open('24-23.txt').read().split('\n')]

def getothers(exc):
    for i in f:
        if i != exc:
            return i
    return -1



#print(f)
visited = []
tly = 0
gps = []

cd = []
for i in range(len(f)):
    for sd in [0,1]:
        if f[i][sd] not in cd:
            cd.append(f[i][sd])
print(cd)

cts = {}
for c in cd:
    cct = []
    for i in f:        
        for lr in [0,1]:
            if i[lr] == c:                
                cct.append(i[1-lr])
    cts[c] = cct

print(cts)
triple = []
bs = {}
lanp = []
for k,v in cts.items():  
    dn = False
    #print(k,v)
    for ct1 in v:  
        #if not dn: # and ct1 not in bs.keys():      
            for ct2 in v:
                #if not dn: # and ct2 not in bs.keys():      
                    if ct2 in cts[ct1]:
                        trp = [k,ct1,ct2]
                        bs[k] = 1
                        bs[ct1] = 1
                        bs[ct2] = 1
                        trp.sort()
                        trpi = (trp[0],trp[1],trp[2])
                        if trpi not in triple:
                            print('adding',trpi)
                            triple.append(trpi)
                            lanp.append(trpi)
                        #else:
                            #print('collision',trpi)
                        dn = True
for i in lanp:
    print(i)
#print(triple)

sts = []
tly = 0
for i in triple:
    ts = 0
    for j in i:
        if j[0] == 't':
            ts += 1
    if ts > 0:
        tly += 1
        print(i)
print(tly)
            
