def load_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    # Remove newline characters
    lines = [line.strip() for line in lines]
    # Transpose lines to a 2D array
    array = [list(line) for line in zip(*lines)]
    return array

def find_start_end(array):
    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return start, end

def convert_to_ordinal(array):
    ordinal_array = [[ord(cell) for cell in row] for row in array]
    return ordinal_array

def find_path_length(array, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        position, length = queue.pop(0)
        if position == end:
            return length
        if position in visited:
            continue
        visited.add(position)
        i, j = position
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < len(array) and 0 <= nj < len(array[0]):
                if array[ni][nj] <= array[i][j] + 1 and (ni, nj) not in visited:
                    queue.append(((ni, nj), length+1))
    # If no path is found, return None
    return None

filename = 'letters2.txt'
array = load_file(filename)
start, end = find_start_end(array)
# Replace 'S' and 'E' with 'a'
array[start[0]][start[1]] = 'a'
array[end[0]][end[1]] = 'a'
ordinal_array = convert_to_ordinal(array)
length = find_path_length(ordinal_array, start, end)
if length is None:
    print("No path found")
else:
    print(f"Length of quickest route: {length}")

#if I had a text file that consists of letters, the file consists of multiple lines.  If I transposed the lines onto a 2 dimensional array.  The 'S' letter is the start coordinate, the 'E' letter is the end coordinate. then replace the 'S' and 'E' characters with the character 'a'.  then replace each letter in the array with the ordinal number of the letter.  If I can only move up, down, left or right on the array, and only if the new number is the same, less or one higher. Write code to find the length of the quickest route from the Start coordinate to the letter End coordinate (plus 4)
