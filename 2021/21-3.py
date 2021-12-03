r = open('21-3.txt').read().split('\n')
#solve times: pt1 - 17mins, pt2 - 25mins (42min total)
ct = [0]*len(r[0])
for i in r:
    for j in range(len(i)):
        if i[j] == '1':
            ct[j] += 1
st,sto = '',''
for i in ct:    
    if i > len(r)/2:
        st += '1'
        sto += '0'
    else: 
        st += '0'
        sto += '1'
print('part 1 -',int(st,2)*int(sto,2))

def getn(r,b):    
    for rf in range(len(r[0])):
        ct = [0]*len(r[0])
        for i in r:
            for j in range(rf,len(i)):
                if i[j] == '1': ct[j] += 1        
        if b == 1:
            if ct[rf] >= len(r)/2: v = '1'
            else: v = '0'
        else:
            if ct[rf] < len(r)/2: v = '1'
            else: v = '0'        
        nr = []    
        for i in r:         
            if i[rf] == v: nr.append(i)    
        r = [i for i in nr[:]]
        if (len(nr) == 1):
            fn = nr[0]
            return(int(fn,2))            

print('part 2 -',getn(r,0)*getn(r,1))
