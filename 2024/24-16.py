
grid = open('24-16.txt').read().split('\n')

# Edited to make it faster, runs in 632ms on Python

from collections import deque
import heapq
import datetime

rows, cols = len(grid), len(grid[0])   

def find_cheapest_path(grid,start,end,best,se):
    
    drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
    Q = []
    if se:
        heapq.heappush(Q, (0, start[0], start[1], 0))        
    else:
        for i in [0,1,2,3]:
            heapq.heappush(Q, (0, start[0], start[1], i))
    visited = set()    
    bestfound = None
    while Q:
        cost, r, c, ld = heapq.heappop(Q)
        
        if (r,c,ld) not in best:
            best[(r,c,ld)] = cost

        if (r, c) == end and bestfound is None:
            bestfound = cost            
        
        if (r, c, ld) in visited:
            continue
        
        visited.add((r, c, ld))       
        
        if se:
            dr,dc = drs[(ld+2)%4]
        else:
            dr,dc = drs[ld]
        nr, nc = r + dr, c +dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':                
            heapq.heappush(Q, (cost + 1, nr, nc, ld))
        heapq.heappush(Q, (cost + 1000, r, c, (ld+1)%4))
        heapq.heappush(Q, (cost + 1000, r, c, (ld+3)%4))
    
    return bestfound  # No path found

a = datetime.datetime.now()
start = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'S')
end = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'E')

bestStarttoEnd = {}
bestEndtoStart = {}
result1 = find_cheapest_path(grid,start,end,bestStarttoEnd,True)
result2 = find_cheapest_path(grid,end,start,bestEndtoStart,False)

print(f"The cheapest path cost is: {result1}")
#print(f"The cheapest path cost is: {result2}")

OK = set()

for r in range(rows):
    for c in range(cols):
        for dir in range(4):
            # (r,c,dir) is on an optimal path if the distance from start to end equals the distance from start to (r,c,dir) plus the distance from (r,c,dir) to end.
            if (r,c,dir) in bestStarttoEnd and (r,c,dir) in bestEndtoStart:
                if bestStarttoEnd[(r,c,dir)] + bestEndtoStart[(r,c,dir)] == result1:
                    OK.add((r,c))
print(len(OK))
b = datetime.datetime.now()
print(b-a)

