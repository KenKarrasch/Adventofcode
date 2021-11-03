c1,c2,f,dp = 0,0,[int(i) for i in open("17-6.txt").read().split()],[]
def dist(f):
    nf,hs = f[:],0    
    for i in range(len(nf))[::-1]:        
        if nf[i] == max(nf): hs = i
    am = nf[hs]
    for j in range(nf[hs]): nf[(hs+j+1)%len(nf)] += 1
    nf[hs] -= am
    return(nf)
while f not in dp[:-1]:    
    f,c1 = dist(f),c1+1
    dp.append(f)    
print('part 1 -',c1)
f = dist(f)
while f != dp[-1:][0]:
    f,c2 = dist(f),c2+1
print('part 2 -',c2+1)
