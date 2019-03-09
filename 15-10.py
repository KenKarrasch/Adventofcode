def frun(s,c):
   l = s[c]
   while c < len(s):
     if s[c] != l:
        return c
     c += 1
   return c

f = open('15-10.txt').read()
ns = [int(i) for i in f]
for i in range(50+1):
  ch,s = 0,ns[:]
  ns = []
  while ch < len(s):
    ct = frun(s,ch)-ch
    ns.append(ct)
    ns.append(s[ch])
    ch += ct
  if i == 40:
   print 'part 1 -',len(s)
print 'part 2 -',len(s)
