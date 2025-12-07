f = open('25-7.txt').read().split('\n')

# Another pretty good rank score for part 1, part 2 less so, changes strategies a few times, I was over-complicating it by using memoisation.
# 7     174    502  **  pt1 
# 7    5170   2713  ***  pt2

tb = []
tbc = {}

DP = {}
tly = 0
for r in range(len(f)):    
    for c in range(len(f[r])):
        if f[r][c] == '^':
            if c in tb:
                tly += 1     
                for d in [-1,1]:       
                    if c+d not in tb:                                                                    
                        tb.append(c+d)   
                        tbc[c+d] = tbc[c] 
                    else:
                        tbc[c+d] += tbc[c]                    
                tb.remove(c)   
                tbc[c] = 0                          
        if f[r][c] == 'S':            
            tb.append(c)
            tbc[c] = 1
        
p = 0
for i in tbc.items():    
    p += i[1]
print(p)
