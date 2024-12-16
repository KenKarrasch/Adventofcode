f = open('24-16.txt').read().split('\n')

grid = []

for i in f:
    ln = []
    for j in i:
        ln.append(j)        
    grid.append(ln)

dr = [(0,1),(1,0),(0,-1),(-1,0)]

nodes = []
s, e = [],[]

visited = []
dts = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            s = [i,j]
        if grid[i][j] == 'E':
            e = [i,j]
        if grid[i][j] == '.':
            dts += 1
            ct = 0
            for d in dr:
                if grid[i+d[0]][j+d[1]] == '.':
                    ct += 1
            if ct > 2:
                nodes.append([i,j])

# [down, right]

print(len(nodes))
print(s,e)
print(len(f),len(f[0]))

Q = [(0,s[0],s[1],0,[])]
print(dts)
dn = False
bpth = []

bst = {}
visited = []

costs = 100000000000000000

while Q and not dn:
    Q.sort(reverse = True)    
    cost,x,y,ld,pth = Q.pop()           

    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):        
        if grid[x][y] != '#':
            skip = False
            #print(x,y,ld)
            if (x,y) not in visited:
                visited.append((x,y))
                print(len(visited),len(list(bst.keys())))                
            if (x,y,ld) in list(bst.keys()):
                if bst[(x,y,ld)] > cost:
                    bst[(x,y,ld)] = cost
                else:
                    skip = True
            else:
                bst[(x,y,ld)] = cost
            if not skip:
                if (x,y) == (e[0],e[1]):   
                    #print(len(visited),dts)                 
                    print('cost',cost)   
                    costs = min(costs,cost)                
                for d in [ld+1,ld+3]:
                    ncost = cost + 1000
                    npth = []
                    for i in pth:
                        npth.append(i[:])                        
                    npth.append([x,y])
                    Q.append([ncost,x,y,(4+d)%4,npth])   
                ncost = cost + 1
                npth = []
                for i in pth:
                    npth.append(i[:])                   
                npth.append([x+dr[ld][0],y+dr[ld][1]])
                Q.append([ncost,x+dr[ld][0],y+dr[ld][1],ld,npth])

print('cost',costs)


