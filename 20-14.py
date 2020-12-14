s = open('20-14.txt').read().split('\n')
# Binary number fun
def am(nm,m,pt):
  u = [i for i in bin(nm)[2:].zfill(36)]
  for i in range(len(u)):
    if '1' in m[i]: u[i] = '1'
    if m[i] == '0t': u[i] = '0'
    if (m[i] in '0') and pt: u[i] = '0'
  st = '0b'
  for i in u: st = st + i
  return int(st,2)

ms2, ms1 = {},{}
for l in range(len(s)):
   c = s[l].split()
   if 'k' in s[l]:
     mk, xb = c[2], []
     for i in range(len(mk)):
        if mk[i] == 'X': xb.append(i)
   else:
     num, mem = int(c[2]),int(c[0][4:-1])
     for i in range(pow(2,len(xb))):
       m = [x for x in mk[:]]
       b = bin(i)[2:].zfill(len(xb))
       for j in range(len(b)):
          m[xb[j]] = b[j] + 't'
       ms2[am(mem,m,0)] = num
     ms1[mem] = am(num,mk,1)
     
print 'part 1 -',sum(ms1.values())
print 'part 2 -',sum(ms2.values())
