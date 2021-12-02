import sys
import collections

# Fun one, drew a map on a piece of paper with room names and items to pick
# then wrote a script for each combination of items until the correct was found.
# used bitwise operators to generate combinations.
# Rank 495/ 1hr27mins

r = list(map(int, open('19-25.txt').read().split(',')))

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
    outputs,dr,rob,op,rb = [],0,(0,0),0,0    
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
      failed = False
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
           line += str(nmap[(x,y)])
          #else:
           #line += '_'            
        print(line)
        if 'Alert!' in line:
          return False
      return True
      

mr = ['east','east','east','north','north','east','north','north','west'] #sec check point

mr = ['north','north','east','east'] # crew quarters
mrb = ['west','west','south','south'] # crew quarters

ml = [['south','west','west'], \
     
     ['take easter egg'], \
     ['east'], \

     ['take fuel cell'], \
     ['east', 'north'], \
     ['north','north','east','east'], \
     
     ['take cake'], \
     ['west','inv','west','south','south'], \
     ['east','south','east','east'], \
     ['west','west','north'], \
      
     ['take ornament'], \
     ['west'], \
     ['east','east'], \
      
     ['take hologram'] , \
     ['east'], \

     ['take dark matter'], \
     ['north','north','east'], \

     ['take klein bottle'],
     ['north'], \

     ['take hypercube'], \
     ['north','west']] #sec check point
mv = [['south','west','west'], \
     ['east'], \
     ['east', 'north','north','north','east','east'], \
     ['west','west','south','south','east','south','east','east','west','west','north'], \
     ['west','east','east'], \
     ['east'], \
     ['north','north','east'], \
     ['north']]
me = ['north','west'] #sec check point
takes = [['take easter egg'], \
     ['take fuel cell'], \
     ['take cake'], \
     ['take ornament'], \
     ['take hologram'] , \
     ['take dark matter'], \
     ['take klein bottle'], \
     ['take hypercube']]

code = [1,0,0,0,1,1,1,0]
#takes = [['take easter egg'], \
#     ['take hologram'] , \
#     ['take dark matter'], \
#     ['take klein bottle']]

if True:
#for a in range[256]:
  #print(a)
  #print('a',a)
  #for b in range(256):
    #print(a&(2**b),a,b)
    
  mr = []
  for m in range(len(mv)):  
    mr = mr + mv[m][:]
    if code[m]:
    #if a&(2**m):
       mr = mr + takes[m][:]
  mr = mr + me  
  print(mr)
  inp = []
  for b in mr:
    for a in range(len(b)):    
      inp.append(ord(b[a]))
    inp.append(10)


  c = docmd(r,inp)
  succ = printmap(c)
  if not succ:
    print('failed')
  else:
    print('okay')
    #break

