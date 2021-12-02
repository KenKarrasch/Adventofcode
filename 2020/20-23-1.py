file = '20-23.txt'
f = open(file).read()
# Part 1 only

print(f)
c = [int(x) for x in f]
for g in range(10,30):
    c.append(g)
print(c)

#print c

i = 0
cn = 0
ln = len(c)
while i < 300:
    i += 1
    #print(c)
    cl = (ln+c[cn]-1)%ln
    if cl == 0: cl = ln
    for n in [1,2,3]:
      for m in [1,2,3]:
        if c[(m+cn)%ln] == cl:
            cl -= 1
            if cl == 0:
                cl = ln
    dest = cl    
    if (cn+4 >= ln):
     pickup = c[cn+1:] + c[:(cn+4)%ln]
    else:     
     pickup = c[cn+1:cn+4]
    #print(cn,'pickup',pickup)
    #print('destination',dest)
    nxt = c[(cn+4)%ln]
    for p in pickup:
     for g in range(ln):
      if g < len(c):
       if c[g] == p:
        c.pop(g)
    for h in range(len(c)):
        if c[h] == dest:
            dc = h        
    for j in [2,1,0]:
       c.insert(dc+1,pickup[j])    
    for j in range(ln):
        if c[j] == nxt:
            diff = (ln + (j - cn - 1))%ln
    c = c[diff:] + c[0:diff]
    #print('')
    cn += 1
    cn = cn%ln
    if i%1000 == 0:
        print(c)
    for y in range(ln):
        if c[y] == 1:
            print(c[y:y+20]) 

print(c)
for y in range(ln):
    if c[y] == 1:
        b = c[y:] + c[0:y]
stri = ''
for x in b[1:]:
    stri = stri + str(x)
print(stri)

# 34675829 too low
