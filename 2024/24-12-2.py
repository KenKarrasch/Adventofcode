
grid = [i for i in open('24-12.txt').read().split('\n')]

# fun one

from collections import defaultdict

bdrs = []

def find_contiguous_groups(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    groups = []

    def dfs(r, c, letter):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] != letter:
            return 0, set()
    
        visited[r][c] = True
        total = 1
        straight_parts = set()
    
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != letter:
                    straight_parts.add((r, c, dr, dc))
                else:
                    sub_total, sub_parts = dfs(nr, nc, letter)
                    total += sub_total
                    straight_parts.update(sub_parts)
            else:
                straight_parts.add((r, c, dr, dc))
    
        return total, straight_parts


    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                total, borders = dfs(r, c, grid[r][c])
                groups.append((grid[r][c], total, borders))

    return groups

def count_adjacent_pairs(tuple_set):
    count = 0
    
    # Convert set to list for easier iteration
    tuple_list = list(tuple_set)
    
    for i, (x1, y1, dx1, dy1) in enumerate(tuple_list):
        for x2, y2, dx2, dy2 in tuple_list[i+1:]:
            # Check if coordinates are adjacent
            #if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            if (abs(x1 - x2) == 0 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 0):
                # Check if velocities are the same
                if dx1 == dx2 and dy1 == dy2:
                    #print(x1, y1, dx1, dy1, '|', x2, y2, dx2, dy2 )
                    count += 1
    
    return count

result = find_contiguous_groups(grid)
tly = 0
for letter, total, borders in result:
    #tly += total * borders
    ct = count_adjacent_pairs(borders)
    #print(letter,borders,len(borders), ct)
    print(f"Group '{letter}': Total letters = {total}, Borders = {len(borders)-ct}")
    tly += total * (len(borders)-ct)
print(tly)
