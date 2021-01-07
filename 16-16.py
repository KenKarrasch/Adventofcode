f = open('16-16.txt').read()

def gchk(ns):
  s = ns[:]
  while len(s)%2 == 0:
    nst = []
    for i in range(int(len(s)/2)):
        nst.append(1-(s[i*2]^s[i*2+1]))
    s = nst[:]    
  return s

tl = 272

ist = [int(x) for x in f]
while len(ist) < tl:
    nist = ist[:] + [0]
    for i in ist[::-1]:
        nist.append(1-i)
    ist = nist[:]    
ist = ist[:tl]
ch = gchk(ist)
stri = ''
for i in ch:
    stri += str(i)
print('part 1 -',stri)

tl = 35651584

ist = [int(x) for x in f]
while len(ist) < tl:
    nist = ist[:] + [0]
    for i in ist[::-1]:
        nist.append(1-i)
    ist = nist[:]
    print(len(ist),'of 35651584')
ist = ist[:tl]
print('calculating checksum')
ch = gchk(ist)
stri = ''
for i in ch:
    stri += str(i)
print('part 2 -',stri)
