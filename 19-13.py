import sys
import collections
# part 1 only
r = list(map(int, open('19-13.txt').read().split(',')))

def pad(st):
  g = ''
  for u in range(5-len(st)): g += '0'
  return g + st

def gmd(m,rb):
    a1 = a2 = a3 = 0
    if m[2] == '2': a1 = rb 
    if m[1] == '2': a2 = rb
    if m[0] == '2': a3 = rb
    return([a1,a2,a3])

for a in [0]:       
    f = collections.defaultdict(lambda: 0, enumerate(r))
    s = a    
    os,ps,dr,rob,op,rb = [],{(0,0):s},0,(0,0),0,0
    d = [[0,-1],[1,0],[0,1],[-1,0]]#ULDR
    while f[op] != 99:
        i = pad(str(f[op]))
        o = i[-2:]
        [a1,a2,a3] = gmd(i[:3],rb)
        if int(o) < 10:
           if i[2] == '1':
              op1 = f[op+1]
           else:
              op1 = f[a1+f[op+1]]
        if int(o) in [1,2,5,6,7,8]:
            if i[1] == '1':
               op2 = f[op+2]
            else:
               op2 = f[a2+f[op+2]]
        if o == '01':
            f[a3+f[op+3]] = op1+op2
            op += 2
        if o == '02':
            f[a3+f[op+3]] = op1*op2
            op += 2
        if o == '03':
             if rob in ps:
              f[a1+f[op+1]] = ps[rob]              
             else:
              f[a1+f[op+1]] = 0
        if o  == '04':
            os.append(op1)
        if o == '05':
            if op1 != 0:
                op = op2 - 2
            else:
                op += 1
        if o == '06':
            if op1 == 0:
               op = op2 - 2
            else:
               op += 1
        if o == '07':
            if op1 < op2:
              f[f[op+3]+a3] = 1
            else:
              f[f[op+3]+a3] = 0
            op += 2
        if o == '08':
            if op1 == op2:
                 f[f[op+3]+a3] = 1
            else:
                 f[f[op+3]+a3] = 0
            op += 2
        if o == '09':
            rb += op1
        op += 2
  
    if a == 0:        
        bls = 0
        print (os)
        for a in range(int(len(os)/3)):          
          if os[(a*3)+2] == 2:
              bls += 1
        print ('part 1 -',bls)

        
        
    
    
      
