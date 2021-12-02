import sys
import collections

# Part 1 - not a, d, not b or c

r = list(map(int, open('19-21.txt').read().split(',')))
sc = open('19-21pt1sc.txt').read().split('\n')

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

def docmd(r,input):
    f = collections.defaultdict(lambda: 0, enumerate(r))
    outputs,rob,op,rb = [],(0,0),0,0       
    inp = input[:]
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
            if len(inp) == 0:                
                return outputs            
            f[a1+f[op+1]] = inp[0]
            inp.pop(0)
        if o  == '04':
            outputs.append(op1)  
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
        if o == '09': rb += op1
        op += 2
    return outputs

def printmap(c):
      x = y = h = 0
      failed = False
      w,nmap = [], {}      
      for g in c:
        if g > 127:
          print('part 1-',g)
          return 0
        if not g == 10:             
         nmap[(x,y)] = chr(g)
         x += 1          
        if g == 10:
          y += 1
          w.append(x)
          x = 0
      h,w = y, max(w)      
      for y in range(h):
        line = ""        
        for x in range(w):
          if (x,y) in nmap:
           line += str(nmap[(x,y)])     
        print(line)

inp = []
for b in sc:
    for a in range(len(b)):
      inp.append(ord(b[a]))
    inp.append(10)
c = docmd(r,inp)
printmap(c)
