f = open('17-9.txt').read()
ns,r = '',0
while r < len(f):
    if f[r] == '!': r += 1
    else: ns += f[r]
    r += 1
r,f,ns,g,gc,lb = 0,ns,'',False,0,False
while r < len(f):
    if f[r] == '<':        
        if not g: lb = True
        g = True                  
    if not g: ns += f[r]
    if g and not lb and f[r] != '>': gc += 1
    if f[r] == '>': g = False            
    r,lb = r+1,False
r,f,ns,d,ct = 0,ns,'',0,0
while r < len(f):
    if f[r] == '{':
        d = d+1
        ct += d    
    if f[r] == '}': d -= 1                        
    r += 1
print('part 1 -',ct)
print('part 2 -',gc)
