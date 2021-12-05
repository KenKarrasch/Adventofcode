r = open('21-5.txt').read().split('\n')
cs = []
for i in r:
    cd = i.split(' -> ')
    cs.append([[int(j) for j in cd[0].split(',')],[int(j) for j in cd[1].split(',')]])

def ad(c):                    
    if c in gd : gd[c] += 1                    
    else: gd[c] = 1  

for pt in [1,2]:
  gd = {}
  for i in cs:
    if i[0][1] == i[1][1]:                
            for r in range(1+abs(i[0][0] - i[1][0])):                        
                if i[0][0] < i[1][0]: ad(i[0][0]+r + (1000*i[1][1]))  
                else: ad(i[1][0]+r + (1000*i[1][1]))                             
    elif i[0][0] == i[1][0]:            
            for r in range(1+abs(i[0][1] - i[1][1])):
                if i[0][1] < i[1][1]: ad(i[0][0] + (1000*(i[0][1]+r)))             
                else: ad(i[1][0] + (1000*(i[1][1]+r)))           
    else:  
        if pt == 2:       
            dx,dy = i[1][0] - i[0][0],i[1][1] - i[0][1]                    
            b = i[0][:] if dx > 0 else i[1][:]
            for r in range(abs(i[0][0] - i[1][0])+1):                           
                if dx*dy > 0: ad(b[0]+r + (1000*(b[1]+r)))                              
                else: ad(b[0]+r + (1000*(b[1]-r)))                             
  print('part',pt,'-',sum([1 for i in list(gd.values()) if i > 1]))  
