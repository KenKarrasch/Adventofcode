f = int(open('16-19.txt').read())
e = [x for x in range(1,f)] + [0]
g,i = e[:],0
while e[i] != i:     
     e[i] = e[e[i]]          
     i = e[i]          
print('part 1 -',i+1)
i = int(f/2)-1
while g[g[i]] != i:     
     g[i] = g[g[g[i]]]
     i = g[i]     
print('part 2 -',i+1)
