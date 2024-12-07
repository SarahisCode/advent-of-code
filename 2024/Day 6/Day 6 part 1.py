from pathlib import Path

def find_index(thing, grid):
    for fpos, line in enumerate(grid):
        for spos, char in enumerate(line):
            if char == thing:
                return (fpos, spos)
    return False

mod_path = Path(__file__).parent
relative_path_1 = 'Day 6 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

grid = [i.strip() for i in input_lines]
height = len(grid)
width = len(grid[0])
visited = []
DIRECTIONS = ((0,1), (1,0), (0,-1), (-1,0))
guard_directions = [">", "v", "<", "^"]
for index, dir in enumerate(DIRECTIONS):
    if find_index(guard_directions[index], grid):
        facing_direction = dir
        guard_pos = list(find_index(guard_directions[index], grid))

def valid(coord):
    return 0 <= coord[0] < height and 0 <= coord[1] < width
while True:
    if guard_pos not in visited:
        visited.append(guard_pos)
    new_x, new_y = guard_pos[0] + facing_direction[0], guard_pos[1] + facing_direction[1]
    if not valid((new_x, new_y)):
        break
    while grid[new_x][new_y] == "#":
        facing_direction = DIRECTIONS[(DIRECTIONS.index(facing_direction)+1)%4]
        new_x, new_y = guard_pos[0] + facing_direction[0], guard_pos[1] + facing_direction[1]
    if not valid((new_x, new_y)):
        break
    guard_pos = [new_x, new_y]
print(len(visited))
    
    

