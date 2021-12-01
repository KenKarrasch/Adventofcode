import math
ns = open('15-14.txt').read().split('\n')
time = 2503
sp = []
for k in ns:
    i = k.split()
    sp.append([int(i[3]),int(i[6]),int(i[13])])
tdsts = []
score = [0 for x in range(len(sp))]
res = []

for t in range(time+1)[1:]:
  md = 0
  bi = -1
  res = []
  for i in sp:
    cy = i[1]+i[2]
    ds = i[0]*i[1]
    rem = t%cy
    cycs = math.floor(t/cy)
    if rem < i[1]:
        tdst = cycs*ds+ rem*i[0]
    else:
        tdst = cycs*ds + i[0]*i[1]
    res.append(tdst)
  for j in range(len(score)):
      if res[j] == max(res):
          score[j] = score[j] + 1        
print('part 1 -',max(res))
print('part 2 -',max(score)) 
