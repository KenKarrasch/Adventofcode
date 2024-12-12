
grid = [i for i in open('24-12.txt').read().split('\n')]

# fun one

from collections import defaultdict

def find_contiguous_groups(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    groups = []

    def dfs(r, c, letter):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] != letter:
            return 0, 0

        visited[r][c] = True
        total = 1
        borders = 0

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != letter:
                    borders += 1
                else:
                    sub_total, sub_borders = dfs(nr, nc, letter)
                    total += sub_total
                    borders += sub_borders
            else:
                borders += 1  # Count edge of grid as border

        return total, borders

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                total, borders = dfs(r, c, grid[r][c])
                groups.append((grid[r][c], total, borders))

    return groups

result = find_contiguous_groups(grid)
tly = 0
for letter, total, borders in result:
    tly += total * borders
    print(f"Group '{letter}': Total letters = {total}, Borders = {borders}")
print(tly)
