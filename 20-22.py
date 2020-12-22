import copy

file = '20-22.txt'
f = open(file).read().split('\n\n')

# quite slow, about a 1 minute to run
# Had trouble dealing with handling infinite loop
# Made use of memoization to save time.

p = []

for i in f:
    p.append([int(x) for x in i.split()[2:]])

r = 2
if True:
 while p[0] and p[1]:
    if p[0][0] > p[1][0]:
        p[0].append(p[0][0])
        p[0].append(p[1][0])
        p[1] = p[1][1:]
        p[0] = p[0][1:]
    else:
        p[1].append(p[1][0])
        p[1].append(p[0][0])
        p[1] = p[1][1:]
        p[0] = p[0][1:]
    r+=1

 for pr in [0,1]:
  ty = 0  
  y = len(p[pr])
  if y > 0:
   for i in range(y):
    ty += y*p[pr][i]
    y += -1
   print ('part 1 -',ty)
 
p = []
for i in f:
    p.append([int(x) for x in i.split()[2:]])

def play(p,depth):
  samedeck = []
  ppl = []
  while p[0] and p[1]:    
    w = -1
    if p in samedeck:       
       return [p[0],[]]
    samedeck.append(copy.deepcopy(p))
    c = [p[0][0],p[1][0]]
    if (c[0]<len(p[0])) and (c[1]<len(p[1])):
       subg = [p[0][1:c[0]+1][:],p[1][1:c[1]+1][:]]
       nw = play(subg,depth+1)
       if len(nw[0])!= 0: w = 1
       else: w = 2
    if w == -1:
      if p[0][0] > p[1][0]: w = 1
      else: w = 2
    if w == 1:        
        p[0].append(p[0][0])
        p[0].append(p[1][0])
        p[1] = p[1][1:]
        p[0] = p[0][1:]
    else:
        p[1].append(p[1][0])
        p[1].append(p[0][0])
        p[1] = p[1][1:]
        p[0] = p[0][1:]
  return copy.deepcopy(p)

play(p,0)

for pr in [0,1]:
  ty = 0  
  y = len(p[pr])
  if y > 0:
   for i in range(y):
    ty += y*p[pr][i]
    y += -1
   print ('part 2 -',ty)

