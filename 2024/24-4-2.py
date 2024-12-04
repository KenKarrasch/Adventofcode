
# Online Python - IDE, Editor, Compiler, Interpreter

g = [i for i in open('24-4.txt').read().split('\n')]

ng = []
for l in g:
    ln = []
    for j in l:
        ln.append(j)
    ng.append(ln)

grid = ng

print(ng)
def find_crossed_word_pattern(grid):
    def check_pattern(i, j, pattern):
        for di in range(3):
            for dj in range(3):
                if i+di >= len(grid) or j+dj >= len(grid):
                    return False
                if pattern[di][dj] != '.' and grid[i+di][j+dj] != pattern[di][dj]:
                    return False
        return True

    patterns = [
        [['M', '.', 'S'],
         ['.', 'A', '.'],
         ['M', '.', 'S']],
        
        [['S', '.', 'M'],
         ['.', 'A', '.'],
         ['S', '.', 'M']],

        [['M', '.', 'M'],
         ['.', 'A', '.'],
         ['S', '.', 'S']],
        
        [['S', '.', 'S'],
         ['.', 'A', '.'],
         ['M', '.', 'M']]
        
    ]

    matches = []
    for i in range(len(grid)-2):
        for j in range(len(grid)-2):
            for pattern in patterns:
                if check_pattern(i, j, pattern):
                    matches.append((i, j, patterns.index(pattern)))

    return len(matches), matches

count, matches = find_crossed_word_pattern(grid)

print('part 2 -',count)

#for match in matches:
 #   print(f"Position: {match[:2]}, Variation: {match[2]}")

# Visualize the matches in the grid
def visualize_matches(grid, matches):
    patterns = [
        [['M', '.', 'S'],
         ['.', 'A', '.'],
         ['M', '.', 'S']],
        
        [['S', '.', 'M'],
         ['.', 'A', '.'],
         ['S', '.', 'M']],

        [['M', '.', 'M'],
         ['.', 'A', '.'],
         ['S', '.', 'S']],
        
        [['S', '.', 'S'],
         ['.', 'A', '.'],
         ['M', '.', 'M']]
    ]
    
    for match in matches:
        print("\nMatch:")
        grid_copy = [row[:] for row in grid]
        i, j, variation = match
        pattern = patterns[variation]
        for di in range(3):
            for dj in range(3):
                if pattern[di][dj] != '.':
                    grid_copy[i+di][j+dj] = pattern[di][dj]
        for row in grid_copy:
            print(' '.join(row))

#visualize_matches(grid, matches)
