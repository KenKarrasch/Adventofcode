r = [3, 7]
er1, er2 = 0, 1
num = open('18-14.txt','r').read()
ended = False
l = len(num)
while not ended:
  newr = r[er1] + r[er2]
  for ch in str(newr):
    r.append(int(ch))
    rstr = ''
    for ch in r[-l:]:
      rstr += str(ch)    
    if rstr == num:
      print 'part 2 -',len(r) - l, r[-1:]
      ended = True      
  er1 = (er1 + r[er1] + 1) % len(r)
  er2 = (er2 + r[er2] + 1) % len(r)
  

r = [3, 7]
er1 = 0
er2 = 1
c = 0
while c < num + 10:
  c += 1
  newr = r[er1] + r[er2]
  for ch in str(newr):
    r.append(int(ch))
  er1 = (er1 + r[er1] + 1) % len(r)
  er2 = (er2 + r[er2] + 1) % len(r)
  
recipe = r[num:num + 10]
print 'part 1 -',recipe
