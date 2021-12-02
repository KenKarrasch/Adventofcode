f = int(open('17-17.txt').read())
z,n,b,l,r,i = 0,0,[0],1,0,1
c = 5000000
for i in range(2018)[1:]:
    r = 1+(r+f)%len(b)
    b = b[:r] + [i] + b[r:]
print 'part 1 -',b[r+1]
r = 0
while i < c*10:
    r,l = 1+(r+f)%l,l+1
    if r < z: z += 1
    if r == z+1: n = i
    if i%c==0: print i
    i += 1
print 'part 2 -',n
