
f = open('24-10.txt').read().split('\n')

grid = []
for i in f:
    ln = []
    for j in i:
        #ln = ln + ' ' + j
        if j != '.':
            ln.append(int(j))
        else:
            ln.append('.')
    grid.append(ln)

print(grid)

import random

def find_unique_paths(grid):
    rows, cols = len(grid), len(grid[0])
    unique_paths = set()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                stack = [(i, j, set())]
                while stack:
                    x, y, visited = stack.pop()
                    if grid[x][y] == 9:
                        unique_paths.add((i, j, x, y))
                        continue
                    
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                            if grid[nx][ny] == grid[x][y] + 1:
                                new_visited = visited.copy()
                                new_visited.add((nx, ny))
                                stack.append((nx, ny, new_visited))
    
    return unique_paths


print("Grid:")
for row in grid:
    print(row)

unique_paths = find_unique_paths(grid)
print(f"\nNumber of unique start-end pairs: {len(unique_paths)}")

print("\nUnique start-end pairs:")
#for start_x, start_y, end_x, end_y in unique_paths:
#    print(f"From (${start_x}, ${start_y}) to (${end_x}, ${end_y})")
