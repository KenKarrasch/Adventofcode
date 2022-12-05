import re
from copy import deepcopy
f = open('22-5.txt').read().split('\n')
b = [[] for i in range(9)]
for i in [x for x in f if '[' in x]:      
  for j in range(9):    
    if(1+j*4 < len(i)):
      if(i[1+j*4] != ' '):                
        b[j].append(i[1+j*4])
for (pt,d) in [(1,-1),(2,1)]:
  g = deepcopy(b)
  for i in [x for x in f if 'to' in x]: 
    sz,s,e = [int(k)-1 for k in re.findall(r'\d+', i)]                        
    g[e] = g[s][:sz+1][::d] + g[e]                
    g[s] = g[s][sz+1:]        
  print('part',pt,'-',''.join(k[0] for k in g))
