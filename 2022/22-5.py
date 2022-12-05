import re
from copy import deepcopy
f = open('22-5.txt').read().split('\n')
b = [[] for i in range(9)]
for i in f:        
    if '[' in i:            
      for j in range(9):    
        ch = 1 + j*4
        if(ch < len(i)):
            if(i[ch] != ' '):                
                b[j].append(i[ch])
for (pt,d) in [(1,-1),(2,1)]:
  g = deepcopy(b)
  for i in f:   
    if 'move' in i:
        sz,s,e = [int(k)-1 for k in re.findall(r'\d+', i)]                        
        g[e] = g[s][:sz+1][::d] + g[e]                
        g[s] = g[s][sz+1:]        
  print('part',pt,'-',''.join(k[0] for k in g))
