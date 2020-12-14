s = open('20-14.txt').read().split('\n')
# binary number fun
def am(nm,m,pt):
  u = [i for i in bin(nm)[2:].zfill(36)]
  for i in range(len(u)):
    if m[i] == '1': u[i] = '1'
    if m[i] == 't1': u[i] = '1'
    if m[i] == 't0': u[i] = '0'
    if m[i] == '0': 
      if pt == 1:  u[i] = '0'
  st = '0b'
  for i in u: st = st + i
  return int(st,2)

ms2, ms1 = {},{}
for l in range(len(s)):
   if 'k' in s[l]:
     mk, xb = s[l].split()[2], []
     for i in range(len(mk)):
        if mk[i] == 'X':
            xb.append(i)
   else:
     num = int(s[l].split()[2])
     mem = int(s[l].split()[0][4:-1])
     for i in range(pow(2,len(xb))):
       m = [x for x in mk[:]]
       b = bin(i)[2:].zfill(len(xb))
       for j in range(len(b)):
         if b[j] == '0': m[xb[j]] = 't0'
         if b[j] == '1': m[xb[j]] = 't1'
       ms2[am(mem,m,2)] = num
     ms1[mem] = am(num,mk,1)
     
print 'part 1 -',sum(ms1.values())
print 'part 2 -',sum(ms2.values())
