from itertools import combinations

g = [i for i in open("24-8.txt").read().split('\n')]

grid = []
anb = []

for i in g:
    ln = []
    lnb = []
    for j in i:
        ln.append(j)
        lnb.append('.')
    grid.append(ln)
    anb.append(lnb)

letter_positions = {}

print(grid)

height = len(grid)
width = len(grid[0])

an = []


# Find positions of all letters
for i in range(height):
    for j in range(width):
        if grid[i][j].isalnum():
            if grid[i][j] not in letter_positions:
                letter_positions[grid[i][j]] = []
            letter_positions[grid[i][j]].append((i, j))

print(letter_positions)

for positions in letter_positions.values():
    if len(positions) >= 2:
            # Generate all possible pairs
        for (y1, x1), (y2, x2) in combinations(positions, 2):
            ltr = grid[y1][x1]
            del_y = y1 - y2
            del_x = x1 - x2
            #print('dxy',del_x,del_y)
            for m in range(max(width,height)):
                for dr in [m,-m]:
                    nx = x1 + (del_x * dr)
                    ny = y1 + (del_y * dr)
                    if 0 <= nx < width and 0 <= ny < height:                    
                            anb[ny][nx] = '#'                        
                    nx = x2 + del_x * dr
                    ny = y2 + del_y * dr
                    if 0 <= nx < width and 0 <= ny < height:                    
                            anb[ny][nx] = '#'
                        
ct  = 0
for i in anb:
    ln = ''
    for j in i:
        ln = ln + j
        if j == '#':
            ct += 1
    print(ln)
print()
print(ct)
