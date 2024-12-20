from pathlib import Path
from copy import deepcopy
import sys

def find_index(thing, grid):
    for fpos, line in enumerate(grid):
        for spos, char in enumerate(line):
            if char == thing:
                return (fpos, spos)

sys.setrecursionlimit(10000)#path is really long

def find_next(pos):
    return ((pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1))

def find_path(pos, path, grid):
    new_grid = deepcopy(grid)
    for new_pos in find_next(pos):
        next_state = grid[new_pos[0]][new_pos[1]]
        if next_state == "E":
            new_path = list.copy(path)
            new_path.append(new_pos)
            return new_path
        if next_state == ".":
            new_grid[new_pos[0]][new_pos[1]] = "#"
            new_path = list.copy(path)
            new_path.append(new_pos)
            print(len(path), new_pos)
            return find_path(new_pos, new_path, new_grid)
        
def find_two_away(pos):
    diag = []
    for i in [-1, 1]:
        for j in (-1, 1):
            diag.append((pos[0]+i, pos[1]+j))
    hori = [(pos[0]+2, pos[1]), (pos[0]-2, pos[1]), (pos[0], pos[1]+2), (pos[0], pos[1]-2)]
    return diag+hori


mod_path = Path(__file__).parent
relative_path_1 = 'Day 20 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

grid = [list(i.strip()) for i in input_lines]

def man_dist(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

start_pos = find_index("S", grid)
path = find_path(start_pos, [start_pos], grid)
at_least_100 = 0
for ind, pos in enumerate(path):
    for after_cheat_pos in find_two_away(pos):
        if after_cheat_pos in path:
            ans = path.index(after_cheat_pos) - ind - 2
            if ans >= 100:
                at_least_100 += 1
print(at_least_100)



    