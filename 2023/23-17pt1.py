
from math import inf 
f = open('23-17.txt').read().split('\n')

g = []
bn = {}

for i in f:
    ln = []    
    for j in i:
        ln.append(int(j))        
    g.append(ln)

dn = False

rs = len(f)
cs = len(f[0])

for i in range(rs):
  for j in range(cs):
    for d in [0,1,2,3]:
      for t in [0,1,2]:
        bn[(i,j,d,t)] = inf

C = [0,1,0,-1]
R = [-1,0,1,0]

DP = {}
ps = [[0,0,0,1,0],[0,0,0,2,0]] #   0heat loss,1r,2c,3direction,4travelled
bn[(0,0,1,0)] = 0
bn[(0,0,2,0)] = 0

ct = 0

dn = False

while not dn:
    ct += 1
    ps.sort()
    #print ('positions',ps)
    p = ps.pop(0)    
    print('looking at p',p,g[p[1]][p[2]] )
    
    if p[1] == rs-1:
      if p[2] == cs-1:
        print('part 1',p[0])
        dn = True         
    for d in [0,1,2,3]:
      if d != (p[3]+2)%4: # Can't turnaround                    
        np = p[:]        
        np[1] += R[p[3]]
        np[2] += C[p[3]]
        #print('np candidate',np)
        if 0 <= np[1] < cs:          
          if 0 <= np[2] < rs:
            if np[3] == d: # direction
               np[4] += 1
            else: np[4] = 0
            np[3] = d        
            np[0] += g[np[1]][np[2]]  # heat loss        
            if np[4] < 3:   
               if (np[1],np[2],d,np[4]) in bn:
                if bn[(np[1],np[2],d,np[4])] > np[0]:
                 bn[(np[1],np[2],d,np[4])] = np[0] # quickest to this square (considering dir and travelled)
                 #print('np',np)
                 ps.append(np)
               else: 
                 # print('np',np)
                 ps.append(np)               
