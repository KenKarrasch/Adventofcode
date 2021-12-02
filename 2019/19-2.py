f = open('19-2.txt').read().split(',')
i = []
for h in f:
    i.append(int(h))
y = i[:]
endresult = 19690720
for u in range(100):
 for v in range(100):
  r = 0
  i = y[:]
  i[1]=u
  i[2]=v
  if(u == 0 and v == 0):
      i[1] = 12
      i[2] = 2
  while i[r] != 99:
    end = False
    if i[r] == 1:
     i[i[r+3]] = i[i[r+1]]+i[i[r+2]]
     end = True
    if not end and (i[r] == 2):
     i[i[r+3]] = i[i[r+1]]*i[i[r+2]]
    r += 4
  if i[0] == endresult:
    print 'part 2 - ',u*100+v
  if(u == 0 and v == 0):
    print 'part 1 - ',i[0]
