# Christmas Encryption Puzzle 
# (originally forgot about the inbuilt pow function)
k1,k2 = [int(x) for x in open('20-25.txt').read().split('\n')]
lp,n = 1,1
while True:
    n,lp = (n*7)%20201227,lp+1
    if n == k2: break    
print('part 1 -',pow(k1,lp-1,20201227))
