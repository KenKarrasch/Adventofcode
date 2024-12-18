from collections import deque

def parse_input(input_str):
    return [tuple(map(int, line.split(','))) for line in input_str.strip().split('\n')]

def simulate_falling_bytes(bytes_list, grid_size=71):
    grid = [[False] * grid_size for _ in range(grid_size)]
    for i, (x, y) in enumerate(bytes_list):
        grid[y][x] = True
        if not has_path(grid):
            return i, (x, y)
    return -1, None

def has_path(grid):
    start = (0, 0)
    end = (len(grid) - 1, len(grid) - 1)
    queue = deque([start])
    visited = set([start])
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and not grid[ny][nx] and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
    
    return False

def solve(input_str):
    bytes_list = parse_input(input_str)
    
    # Part 1
    grid = [[False] * 71 for _ in range(71)]
    for x, y in bytes_list[:1024]:
        grid[y][x] = True
    
    start = (0, 0)
    end = (70, 70)
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            part1_result = steps
            break
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and not grid[ny][nx] and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))
    
    # Part 2
    _, critical_byte = simulate_falling_bytes(bytes_list)
    part2_result = f"{critical_byte[0]},{critical_byte[1]}"
    
    return part1_result, part2_result

input_str = open('24-18.txt').read()

part1, part2 = solve(input_str)
print(f"Part 1: Minimum number of steps needed to reach the exit: {part1}")
print(f"Part 2: Coordinates of the first byte that prevents reaching the exit: {part2}")
