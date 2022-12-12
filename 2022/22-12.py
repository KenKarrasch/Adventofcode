import copy
# Breadth First Search, part 2 searches backwards from z

f = open('22-12.txt').read().split('\n')

s = []
e = []
g = []
for i in range(len(f)):
  l = []
  for j in range(len(f[i])):
    if f[i][j] == 'S':
      s = [i,j]
    if f[i][j] == 'E':
      e = [i,j]
    l.append(ord(f[i][j]))
  g.append(l)

drs = [[0,1],[0,-1],[1,0],[-1,0]]

bst = []

for i in range(len(g)): 
    b = []
    for j in range(len(g[0])):
      b.append(1000000)
    bst.append(b)   
bst[s[0]][s[1]] = 0

g[s[0]][s[1]] = ord('a')-1
g[e[0]][e[1]] = ord('z')

bst[s[0]][s[1]] = 0

cd = -1
done = False
while not done:
 cd += 1
 for i in range(len(bst)):    
  for j in range(len(bst[0])):        
    if bst[i][j] == cd:      
      ht = g[i][j]
      for d in drs:     
        ns = i+d[0],j+d[1]
        if 0 <= ns[0] < len(g): 
          if 0 <= ns[1] < len(g[0]):              
            if [i,j] == e:
              done = True
              print('part 1 -',cd)
              break            
            if g[ns[0]][ns[1]] <= ht + 1:            
              if bst[ns[0]][ns[1]] > cd+1:            
                bst[ns[0]][ns[1]] = cd + 1

g = []
for i in range(len(f)):
  l = []
  for j in range(len(f[i])):
    if f[i][j] == 'S':
      s = [i,j]
    if f[i][j] == 'E':
      e = [i,j]
    l.append(1+ord('z') - ord(f[i][j]))
  g.append(l)

bst = []

for i in range(len(g)): 
    b = []
    for j in range(len(g[0])):
      b.append(1000000)
    bst.append(b)   

g[s[0]][s[1]] = ord('z')-1
g[e[0]][e[1]] = 0

bst[e[0]][e[1]] = 0

cd = -1
done = False
while not done:
 cd += 1
 for i in range(len(bst)):    
  for j in range(len(bst[0])):        
    if bst[i][j] == cd:      
      ht = g[i][j]
      for d in drs:     
        ns = i+d[0],j+d[1]
        if 0 <= ns[0] < len(g): 
          if 0 <= ns[1] < len(g[0]):              
            if ht == 26:
              print('part 2 -',cd)
              done = True
              break        
            if g[ns[0]][ns[1]] <= ht + 1:            
              if bst[ns[0]][ns[1]] > cd+1:            
                bst[ns[0]][ns[1]] = cd + 1

