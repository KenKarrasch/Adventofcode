f = open('25-7.txt').read().split('\n')

# 7     174    502  **

tb = []
tly = 0
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == '^':            
            if j in tb:
                tly += 1            
                if j+1 not in tb:                    
                    tb.append(j+1)                    
                if j-1 not in tb:
                    tb.append(j-1)                    
                tb.remove(j)            
        if f[i][j] == 'S':            
            tb.append(j)        
print(tly)
