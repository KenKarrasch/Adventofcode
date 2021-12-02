import itertools
r = [int(n) for n in open('19-7.txt').read().split(',')]

def pad(st):
  g = ''
  for u in range(5-len(st)): g += '0'
  return g + st

def a(i,n,op,f):  
  if i[3-n] == '0':
    return(f[f[op+n]])
  else: return(f[op+n])

def doamp(input,op):
    f = r[:]
    while True:
      i = pad(str(f[op]))     
      o = i[-2:]
      if op + 1 < len(f):        
        a1 = f[op+1]
      else:
        a1 = 0
      if op + 3 < len(f):        
        a3 = f[op+3]
      else: a3 = 0
      if o == '01':
        f[a3] = a(i,1,op,f)+a(i,2,op,f)        
        op += 2
      if o == '02':
        f[a3] = a(i,1,op,f)*a(i,2,op,f)
        op += 2
      if o == '03':
        f[a1] = input[0]
        input.pop(0)        
      if o == '04':
        output = f[a1]
        return output, op + 2   
      if o == '05':
          if a(i,1,op,f): op = a(i,2,op,f)-2
          else: op += 1
      if o == '06':
          if a(i,1,op,f): op += 1
          else: op = a(i,2,op)-2
      if o == '07':
          if a(i,1,op,f) < a(i,2,op,f): f[a3] = 1
          else: f[a3] = 0
          op += 2
      if o == '08':
          if a(i,1,op,f) == a(i,2,op,f): f[a3] = 1
          else: f[a3] = 0
          op += 2
      if o == '99':
          return None, op + 2
      op += 2

thrust = []
for p in [[5,6,7,8,9]]:
  for phase in itertools.permutations(list(p), 5):
   ph_combo = [u for u in phase]
   opcode,f5,inputs  = [0,0,0,0,0],[0,1,2,3,4],[]
   ao = opcode[:]#ampout
   for c in f5:
     p = [ph_combo[c]]
     if c == 0:
       p.append(0)
     inputs.append(p)
   end = False
   while not end:
    for amp in f5:
      output,new_ip = doamp(inputs[amp],opcode[amp])  
      if output == None:
          thrust.append(ao[-1])         
          end = True
          break
      opcode[amp] = new_ip
      if output != None:
           ao[amp] = output
      if(amp == 4):#feedback
        inputs[0].append(output)
      else:
        inputs[amp+1].append(output)
print('part 2 - ',max(thrust))
