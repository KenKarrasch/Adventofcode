f = open('23-9.txt').read().split('\n')
# Super easy one today
print(f)
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
    print(sqs)
    sqsb.append(sqs)

ty = 0

for sqs in sqsb:
   am = 0
   print('sqs',sqs)
   for sq in sqs[::-1]:
        print('sq',sq)        
        am = sq[0] - am
        print('am',am)         
   ty += am
print(ty)
