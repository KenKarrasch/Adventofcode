import sys
import collections

# Fairly straightforward once I displayed the output properly.
# Tried to do it manually by parts, but arithmetic failed me.

r = list(map(int, open('19-17.txt').read().split(',')))

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

def docmd(r,input,mode):
    f = collections.defaultdict(lambda: 0, enumerate(r))
    outputs,dr,rob,op,rb = [],0,(0,0),0,0
    f[0] = mode
    ps = {(0,0):4}
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
      w,nmap = [], {}      
      for g in c:
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
           line += str(nmap[(x,y)])+' '
          else:
           line += '_'            
        print(line)
      return nmap

c = docmd(r,[],1)
nmap = printmap(c)
amt = 0
for a in nmap.keys():
  x = a[0]
  y = a[1]        
  if ((x+1,y) in nmap) and\
     ((x-1,y) in nmap) and\
     ((x,y+1) in nmap) and\
     ((x,y-1) in nmap):
   if nmap[(x,y)] != '#': continue
   if nmap[(x+1,y)] == nmap[(x-1,y)] == nmap[(x,y+1)] == nmap[(x,y-1)] == '#':
     amt += x*y
print('part 1 -',amt)

full = 'R,10,R,8,L,10,L,10, R,8,L,6,L,6, R,8,L,6,L,6, R,10,R,8,L,10,L,10, L,10,R,10,L,6, R,8,L,6,L,6, L,10,R,10,L,6, L,10,R,10,L,6, R,8,L,6,L,6, R,10,R,8,L,10,L,10'
       # A                  B            B            A                   C              B            C              C              B            A

mr = ['A,B,B,A,C,B,C,C,B,A',\
      'R,10,R,8,L,10,L,10', \
      'R,8,L,6,L,6', \
      'L,10,R,10,L,6', \
      'n']

inp = []
for b in mr:
  for a in b: inp.append(ord(a))
  inp.append(10)
c = docmd(r,inp,2)
print('part 2 -',c[-1:])
