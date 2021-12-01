f = open('16-9.txt').read()

def getd(st):
    ds = ''
    c = 0
    fd = False
    while True:
      if st[c] == ')':
        break
      ds += st[c]
      c += 1
    return ds.split('x')+[c]

ns,c = '',0
while c in range(len(f)):
    if f[c] not in '(':
        ns += f[c]
    else:
        [lts,dup,ln] = getd(f[c+1:])
        #print(ns,lts,dup,ln)
        for i in range(int(lts)*int(dup)):
            ns += 'x'
        c += ln+int(lts)+1
    c += 1
print('part 1 -',len(ns))

def getchc(st,depth):
  c,ct = 0,0
  while c in range(len(st)):
    if st[c] not in '(':        
        ct += 1
    else:        
        [lts,dup,ln] = getd(st[c+1:])        
        ct += int(dup)*getchc(st[c+ln+2:c+ln+int(lts)+2],depth+1)
        c += ln+int(lts)+1
    c += 1
  return ct

print('part 2 -',getchc(f,0))
