import sys
import collections

# This is a synchronous solution. I figured it would work as there is no
# gaurantee of when the processes will finish, and send their outputs.
# The solution runs through each process, and does only one at a time,
# input or output.  Then saves it state, then moves onto the next processor.

r = list(map(int, open('19-23.txt').read().split(',')))

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

def runp(f,n,op):
    global inp
    global out
    rb = term = gobble = 0
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
            if term > 3:
              f[a1+f[op+1]] = -1
              return f, op+2
            if len(inp[n]) != 0:
              f[a1+f[op+1]] = inp[n][0]
              if not (inp[n][0] == n):
                  gobble += 1              
            else:
              f[a1+f[op+1]] = -1
              term += 1            
            if len(inp[n]) != 0:
              inp[n].pop(0)              
            if gobble == 1:
                return f, op+2
        if o  == '04':
            out.append(op1)
            if len(out) == 3:
               return f, op+2
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
      
      
f = collections.defaultdict(lambda: 0, enumerate(r))
out,inp,nat,op,fs = [],[],[],[],[]
lasty = idlect =0
for a in range(50):
    inp.append([a])
    op.append(0)
    fs.append(f.copy())
p = cy = 0
rd = 1
end = pt1 = False
while not end:
  rd += 1
  for a in range(50):
    if p > len(op)-1:
        p = 0
        cy += 1
    fo,opo = runp(fs[p],p,op[p])
    fs[p] = fo.copy()
    op[p] = opo
    p += 1
    for a in range(int(len(out)/3)):
        if out[a*3] == 255:
          nat = out[a*3+1:a*3+3]
          if not pt1:
              print('part 1 -',nat[1])
              pt1 = True
          if lasty == nat[1]:
            print ('part 2 -',lasty)
            end = True
        else:
          inp[out[a*3]].append(out[a*3+1])
          inp[out[a*3]].append(out[a*3+2])
    out = []
  ict = 0
  for i in inp:
    ict += len(i)    
  if ict == 0:
   if len(nat) > 0:
    idlect += 1
    if idlect > 4:
      inp[0].append(nat[0])
      inp[0].append(nat[1])
      lasty = nat[1]
      idlect = 0

