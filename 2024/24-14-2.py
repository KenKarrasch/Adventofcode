
f = open('24-14.txt').read().split('\n')
import re
md = []

# Pretty Christmas Tree, Works out when contiguous groups of robots is less than 200.

from collections import defaultdict, Counter, deque

for i in f:
    numbers = re.findall(r'-?\d+', i)
    md.append(list(map(int, numbers)))
#print(md)


def update_position(robot, W, H, time, grid):
    x, y, vx, vy = robot
    new_x = (x + vx * time) % W
    new_y = (y + vy * time) % H    
    grid[new_y][new_x] = '#'
    return (new_x, new_y, vx, vy)

W, H = 11, 7 # Room dimensions
W, H = 101, 103 # Room dimensions

time = 100  # Seconds to simulate

# List of robots with initial positions and velocities
robots = []

for i in md:
    robots.append((i[0],i[1],i[2],i[3]))    


drs = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

dn = False
while not dn:    
    grid = [['.' for x in range(W)] for y in range(H)]
    time += 1
    updated_robots = []
    for robot in robots:        
        updated_robots.append(update_position(robot, W, H, time, grid))

    tree = False

    components = 0
    visited = set()
    for x in range(W):
        for y in range(H):
            if grid[y][x] == '#' and (x,y) not in visited:
                sx,sy = x,y
                components += 1
                Q = deque([(sx,sy)])
                while Q:
                    x2,y2 = Q.popleft()
                    if (x2,y2) in visited:
                        continue
                    visited.add((x2,y2))
                    for dx,dy in drs:
                        xx,yy = x2+dx,y2+dy
                        #grid[yy][xx]
                        if 0<=xx<W and 0<=yy<H and grid[yy][xx]=='#':
                            Q.append((xx,yy))
    if time%1000 == 0:
        print(time)
    if components <= 200:        
        gstr = []
        for row in grid:
            gstr.append(''.join(row))
        print('\n'.join(gstr))
        dn = True
        print(time)
        break
    
