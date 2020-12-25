# Christmas Encryption Puzzle
k1,k2 = [int(x) for x in open('20-25.txt').read().split('\n')]
lp,n = 1,1
while True:
    n,lp = (n*7)%20201227,lp+1
    if n == k2: break    
n = 1
for i in range(lp-1):
    n = (n*k1)%20201227
print('part 1 -', n)
