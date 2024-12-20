from collections import deque

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

    ct, ln = 0, 0    
    for de in list(DE.keys()):
        print(ln, 'of', 9352)
        ln += 1
        for ds in list(DS.keys()):
            if abs(de[0] - ds[0]) + abs(de[1] - ds[1]) <= 20:
                if DE[de] + DS[ds] + abs(de[0] - ds[0]) + abs(de[1] - ds[1]) <= nocheatd - 100:
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
