f = open('21-10.txt').read().split('\n')

c = [['(',')'],['[',']'],['{','}'],['<','>']]
a = [3,57,1197,25137]
vl = [1,2,3,4]
s = [0,0,0,0]
uw = []
 
def gv(l):
   sk = []
   for ch in l:
     for t in [0,1,2,3]:
       if ch == c[t][0]:
         sk.append(ch)
       else:
         if ch == c[t][1]:
           if sk[-1] != c[t][0]:
            return a[t]
           else:
            sk.pop()
   uw.append(sk)
   return 0
        
tl = 0
for i in range(len(f)):
   tl += gv(f[i])
print 'part 1 -',tl
scs = []
for sk in uw:
   nv = 0
   for ch in sk[::-1]:
     for t in [0,1,2,3]:
       if ch == c[t][0]:
           nv *= 5
           nv += vl[t]
   scs.append(nv)
scs.sort()
print 'part 2 -',scs[int(len(scs)/2)]
