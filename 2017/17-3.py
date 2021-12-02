inp = int(open('17-3.txt').read())
# Had some fun with dictionaries
di = [[0,1],[1,0],[0,-1],[-1,0]]
ch = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
cd,s,cx,cy,ct1,ct2,dc  = 1,1,0,0,2,0,{0:1}
fd1,fd2 = False,False
while not fd1 or not fd2: 
    for j in [0,1]:
        for i in range(s):
            cx += di[cd][0]
            cy += di[cd][1]            
            if(ct1 == inp) and not fd1:
                print('part 1 -',abs(cx)+abs(cy))  
                fd1 = True          
            ct1,ct2 = ct1 + 1,0            
            for sc in ch:
                if (cx+sc[0])*10000+(cy+sc[1]) in dc:                
                    ct2 += dc[(cx+sc[0])*10000+(cy+sc[1])]                
            dc[cx*10000+cy] = ct2
            if(ct2 > inp) and not fd2:
                print('part 2 -',ct2)
                fd2 = True                            
        cd = (cd + 1) % 4    
    s += 1  
