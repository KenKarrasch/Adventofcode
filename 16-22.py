dev = open('16-22.txt').read().split('\n')
x = []
y = []
used = []
av = []

for i in dev[2:]:
    fi = i.split()
    nd = fi[0].split('-')    
    x.append(int(nd[1][1:]))
    y.append(int(nd[2][1:]))
    used.append(int(fi[2][:-1]))
    av.append(int(fi[3][:-1]))

via = 0
for i in range(len(x)):
    for j in range(len(x)):
     if i != j:
      if (used[i] <= av[j]):
        if used[i] != 0:  
         via += 1

gr = [['.' for i in range(max(y)+1)] for j in range(max(x)+1)]
gr[0][0] = 'P'
gr[max(x)][0] = 'G'

mh = max(x)  # max height (length of the # wall)

for i in range(len(x)):    
    if used[i] > 100:      
      gr[x[i]][y[i]] = '#'
      if x[i] < mh:
          mh = x[i]          
    if used[i] == 0:      
      gr[x[i]][y[i]] = '_'
      us = [x[i],y[i]]  # location of underscore

st = ''
print('012345678901234567890123456789')
for i in range(max(x)+1):
    print(st.join(gr[i]),i)
dist = 0
dist += us[0]-(mh-1) #up over the wall
dist += us[1] #left to g
dist += us[0]  #down to g
dist += 5*(max(x)-1) # 5 steps per pull up
dist -= 1 # out by one error
print('part 1 -',via)
print('part 2 -',dist)
