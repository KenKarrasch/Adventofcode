
f = open('24-10.txt').read().split('\n')

# got part 2 out accidentally before part 1

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

def find_paths(grid):
    rows, cols = len(grid), len(grid[0])
    all_paths = []
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                stack = [(i, j, [(i, j)])]
                while stack:
                    x, y, path = stack.pop()
                    if grid[x][y] == 9:
                        all_paths.append(path)
                        continue
                    
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in path:
                            if grid[nx][ny] == grid[x][y] + 1:
                                new_path = path + [(nx, ny)]
                                stack.append((nx, ny, new_path))
    
    return all_paths

paths = find_paths(grid)
print(f"\nNumber of paths: {len(paths)}")

print("\nPaths:")
