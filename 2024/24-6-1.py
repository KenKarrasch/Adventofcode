f = open("24-6.txt").read().split('\n')


grid = []
for l in f:
    ln = []
    for j in l:
        ln.append(j)
    grid.append(ln)

print(grid)

def simulate_walk(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    dir_index = 0
    
    # Find the starting position
    start_pos = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                start_pos = (i, j)
                break
        if start_pos:
            break
    
    if not start_pos:
        return 0, grid  # No starting position found
    
    x, y = start_pos
    steps = 0
    path = grid.copy()
    
    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        dx, dy = directions[dir_index]
        new_x, new_y = x + dx, y + dy
        
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if grid[new_x][new_y] == '#':
                dir_index = (dir_index + 1) % 4  # Turn right
            else:
                x, y = new_x, new_y
                steps += 1
                if path[x][y] == '.':
                    path[x][y] = '*'
        else:
            break  # Off the map
    
    return steps, path


steps, path = simulate_walk(grid)
print(f"The person traveled {steps} steps before going off the map.")

print("\nPath taken:")
ct = 0
for row in path:
    for ch in row:
        if ch in '^*':
            ct += 1      
    print(''.join(row))
    
print(ct)
