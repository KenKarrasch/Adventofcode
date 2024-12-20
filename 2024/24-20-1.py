from collections import deque

# Tried it a different way, create a map of how far it is to the start, and another map of how far it is to the end. The go though the grid if there is a '#' 
# check either side of it, and up and down, it they are '.', then compare the (dist to end + dist to start + 2 <= no cheat distance - 100)

def solve(grid):    
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[c][r] == 'S':
                start = (r,c)
            if grid[c][r] == 'E':
               end = (r,c)
    print(start,end)

    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            nocheatd = steps
            break       
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not grid[ny][nx] == '#' and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))
    print(nocheatd)
    queue = deque([(end, 0)])       
    DE = {} # distance from the end
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) in DE:
            continue            
        DE[(x,y)] = steps 
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not grid[ny][nx] == '#':
                queue.append(((nx, ny), steps + 1))                                
    #print(DE)
    queue = deque([(start, 0)])  
    DS = {} # distance from the start
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) in DS:
            continue            
        DS[(x,y)] = steps 
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not grid[ny][nx] == '#':
                queue.append(((nx, ny), steps + 1))   
    #print(DS)
    ct = 0
    for r in range(1,len(grid)-1):
        print('row',r,ct)
        for c in range(1,len(grid[0])-1):            
            if 0 <= r < R and 0 <= c < C and grid[c][r] == '#':             
                for swap in [1]:
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: 
                        if (r-dx*swap,c-dy*swap) in list(DE.keys()) and (r+dx*swap,c+dy*swap) in list(DS.keys()):
                            if DE[(r-dx*swap,c-dy*swap)] + DS[(r+dx*swap,c+dy*swap)] + 2 <= nocheatd - 100:
                                ct += 1
    print(ct)

 
ins = open('24-20.txt').read().split('\n')
gd = []
for i in ins:
    ln = []
    for j in i:
        ln.append(j)
    gd.append(ln)
solve(gd)


# 1289
# 982424
