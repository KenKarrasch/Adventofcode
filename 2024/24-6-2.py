f = open("24-6.txt").read().split('\n')

# Online compiler had limitations on run time, had to do it by parts.

grid = []
for l in f:
    ln = []
    for j in l:
        ln.append(j)
    grid.append(ln)

#print(grid)

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
    #path = [row[:] for row in grid]  # Create a deep copy of the grid
    visited = set()  # To keep track of visited positions and directions
    
    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        current_state = (x, y, dir_index)
        if current_state in visited:
            return -1, path  # Circular path detected
        visited.add(current_state)
        
        dx, dy = directions[dir_index]
        new_x, new_y = x + dx, y + dy
        
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if grid[new_x][new_y] == '#':
                dir_index = (dir_index + 1) % 4  # Turn right
            else:
                x, y = new_x, new_y
                steps += 1
                #if path[x][y] == '.':
                    #path[x][y] = '*'
        else:
            break  # Off the map
    
    return steps, -1 #path


gr = [row[:] for row in grid]
    

print(len(grid))
print(len(grid[0]))

infi = 0

tly = 0

for i in range(len(grid[0])):    
    for j in range(len(grid)):
        grid = [row[:] for row in gr]
        
        path = grid.copy()
        grid[j][i] = '#'
        steps, path = simulate_walk(grid)
        if steps == -1:
            #print('inf')
            infi += 1
          
    print('line',i,infi)
    tly += infi
    infi = 0
print(tly)

