r = [int(n) for n in open('19-5.txt').read().split(',')]

input,output,op = 1,0,0

def pad(st):
  g = ''
  for u in range(5-len(st)): g += '0'
  return g + st

def a(i,n):
  if i[3-n] == '0': return(f[f[op+n]])
  else: return(f[op+n])
    
for g in [1,2]:
 input,output,op,f = (4*g)-3,0,0,r[:]
 while f[op] != 99:
  i = pad(str(f[op]))
  o, a1, a3 = i[3:], f[op+1], f[op+3]
  if o == '01':
    f[a3] = a(i,1)+a(i,2)
    op += 2
  if o == '02':
    f[a3] = a(i,1)*a(i,2)
    op += 2
  if o == '03':
    f[a1] = input
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
 print 'part',g,'-',output
