f = open('23-9.txt').read().split('\n')
# super easy one today
sqsb = []
for s in f:
    sqs = []
    sq = [int(y) for y in s.split()]
    sqs.append(sq[:])    
    pos = 0
    dn = False
    while not dn:
      ns = []
      for i in range(len(sqs[pos])-1):
        ns.append(sqs[pos][i+1]-sqs[pos][i])      
      sqs.append(ns)    
      if ns.count(0) == len(ns):
         dn = True
      pos += 1    
    sqsb.append(sqs)
pt2 = pt1 = 0

for sqs in sqsb:
   d2 = d1 = 0   
   for sq in sqs[::-1]:        
        d2 = sq[0] - d2                
        d1 += sq[-1]    
   pt2 += d2
   pt1 += d1

print('part 1',pt1)
print('part 2',pt2)
