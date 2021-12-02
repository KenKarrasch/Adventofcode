m = [i for i in open('17-19.txt').read().split('\n')]

sz,p,dn,dr,pl,s = [len(m[0]),len(m)],[0,0],False,2,'',0 
d = [[0,-1],[1,0],[0,1],[-1,0]] #NESW
for i in range(len(m[1])): #Find the starting point
    if m[0][i] == '|': p[0] = i

def gp(p,o):
    n = [p[0] + o[0],p[1] + o[1]]
    if n[0] < sz[0] and n[0] > -1 and n[1] < sz[1] and n[1] > -1:
        return m[n[1]][n[0]]
    return '#'

while not dn:
    if m[p[1]][p[0]] not in '+|- ': pl += m[p[1]][p[0]]
    if gp(p,d[dr]) != '#':                
        p = [p[0] + d[dr][0],p[1] + d[dr][1]]        
        s += 1            
    if gp(p,[0,0]) in '+ ':        
        dn = True
        for j in [(dr+1)%4,(dr+3)%4]:            
            if gp(p,d[j]) != ' ':                    
                dr = j
                dn = False        
print('part 1 -',pl)
print('part 2 -',s)
