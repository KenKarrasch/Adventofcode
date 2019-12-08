import itertools

r = [int(n) for n in open('19-7.txt').read().split(',')]

input,output,op = 1,0,0

def pad(st):
  g = ''
  for u in range(5-len(st)): g += '0'
  return g + st

def a(i,n):
  if i[3-n] == '0': return(f[f[op+n]])
  else: return(f[op+n])

output = 0

g = 2
for p in [[0,1,2,3,4]]:
  res = []
  for phase in itertools.permutations(list(p), 5):
   output = 0
   for ph in range(len(phase)):     
     input = [phase[ph],output]
     output,op,f = 0,0,r[:]
     innum = 0
     while f[op] != 99:
      i = pad(str(f[op]))     
      o, a1, a3 = i[-2:], f[op+1], f[op+3]
      if o == '01':
        f[a3] = a(i,1)+a(i,2)
        op += 2
      if o == '02':
        f[a3] = a(i,1)*a(i,2)
        op += 2
      if o == '03':
        f[a1] = input[innum]
        innum += 1
      if o == '04':
        output = f[a1]
      if g == 2:
        if o == '05':
          if a(i,1): op = a(i,2)-2
          else: op += 1
        if o == '06':
          if a(i,1): op += 1
          else: op = a(i,2)-2
        if o == '07':
          if a(i,1) < a(i,2): f[a3] = 1
          else: f[a3] = 0
          op += 2
        if o == '08':
          if a(i,1) == a(i,2): f[a3] = 1
          else: f[a3] = 0
          op += 2
      op += 2     
   res.append(output)
  print('part 1 -',max(res))
