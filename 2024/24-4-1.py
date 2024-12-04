
# Online Python - IDE, Editor, Compiler, Interpreter

# Took way longer than hoped.

g = [i for i in open('24-4.txt').read().split('\n')]

ng = []
for l in g:
    ln = []
    for j in l:
        ln.append(j)
    ng.append(ln)

grid = ng

print(ng)
def find_word_occurrences(grid, word):
    def search_direction(i, j, di, dj):
        for letter in word:
            if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or
                grid[i][j] != letter):
                return False
            i += di
            j += dj
        return True

    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    matches = []

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == word[0]:
                for di, dj in directions:
                    if search_direction(i, j, di, dj):
                        match = [(i + k*di, j + k*dj) for k in range(len(word))]
                        matches.append(match)

    return len(matches), matches

word = "XMAS"
count, matches = find_word_occurrences(grid, word)

print(f"The word '{word}' appears {count} times in the grid.")
print("Matches found at:")
#for match in matches:
#    print(match)

# Visualize the matches in the grid
def visualize_matches(grid, matches):
    for match in matches:
        print("\nMatch:")
        grid_copy = [row[:] for row in grid]
        for i, j in match:
            grid_copy[i][j] = grid_copy[i][j].lower()  # Highlight matched letters
        for row in grid_copy:
            print(' '.join(row))

#visualize_matches(grid, matches)
