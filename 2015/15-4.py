import hashlib
f = open('15-4.txt').read()
n,fd,fd1 = 0,False,False
while not fd:
 n += 1
 c = f + str(n)
 o = hashlib.md5(c).hexdigest()
 if o[:5] == '00000':
   if not fnd:
     print 'part 1 - ',n
     fnd = True
 if o[:6] == '000000':
     print 'part 2 - ',n
     fd = True
