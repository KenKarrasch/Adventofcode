f1 = [int(i) for i in open('17-5test.txt').read().split()]
ct,pt,o,f = 0,0,0,f1[:]
while pt < len(f):        
    pt += f[o]
    f[o],o,ct = f[o]+1,pt,ct+1     
print ('part 1 -',ct)  
ct,pt,o,f = 0,0,0,f1[:]
while pt < len(f):          
    pt += f[o]
    f[o],ct,o = f[o]+1-(2*(f[o]>2)),ct+1,pt    
print ('part 2 -',ct)
