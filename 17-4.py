f,p1,p2 = [i.split() for i in open("17-4.txt").read().split('\n')],0,0
for i in f:            
    c2,c1,l = 1,1,range(len(i))
    for j in l:                  
        for u in l:            
            if u != j:                                          
                us = [c for c in i[u]]                
                us.sort()                
                js = [c for c in i[j]]                
                js.sort()                 
                if us == js: c2 -= (c2 == 1)
                if i[u] == i[j]: c1 -= (c1 == 1)                
    p1,p2 = p1+c1,p2+c2
print('part 1 -',p1,'part 2 -',p2)
