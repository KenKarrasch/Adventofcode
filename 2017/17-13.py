f = open("17-13.txt").read().split('\n')
fn = {}
for i in f:
    n = i.split(': ')
    fn[int(n[0])] = int(n[1])
k = list(fn.keys())
p = [0 for i in range(max(k)+1)]
de = [1 for i in range(len(p))]
for i in range(len(p)):
    if i not in k: p[i] = -1

def go(fn,p,de):
    d = 0    
    for j in range(len(p)):                 
        if j in k:
                if p[j] == 0: d += j*fn[j]        
        for i in range(len(p)):
            if p[i] != -1:        
                if p[i] == fn[i]-1:
                    if de[i] == 1: de[i] = -1
                if p[i] == 0:
                    if de[i] == -1: de[i] = 1
                p[i] += de[i]   
    return(d)

def gofast(dl,fn,p):     
    for i in range(len(p)):
        if i in list(fn.keys()):
            if (i+dl)%((fn[i]-1)*2) == 0: return False
    return True

print('part 1 -',go(fn,p,de))
dl = 1
while True:
    if gofast(dl,fn,p):
        print('part 2 -',dl)
        break
    dl += 1
    if dl%10000 == 0: print(dl)
