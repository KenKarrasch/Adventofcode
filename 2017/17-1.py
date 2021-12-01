f = [int(i) for i in open('17-1.txt').read()]
t1,t2,l = 0,0,len(f)
for i in range(len(f)):
    if f[i-1] == f[i]:
        t1 += f[i]    
    if f[i] == f[(i + int((l+1)/2))%l]:
        t2 += f[i]
print('part 1 - ', t1, ', part 2 - ',t2)
