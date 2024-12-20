from pathlib import Path
from copy import deepcopy
import sys
import time

def find_index(thing, grid):
    for fpos, line in enumerate(grid):
        for spos, char in enumerate(line):
            if char == thing:
                return (fpos, spos)

sys.setrecursionlimit(10000)#path is really long

def find_next(pos):
    return ((pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1))

def find_path(pos, path, grid):
    for new_pos in find_next(pos):
        if len(path) > 1:
            if path[-2] == new_pos:
                continue
        #sound is off because of call
        #why is it going back and forth
        #-2 because -1 is current position
        next_state = grid[new_pos[0]][new_pos[1]]
        if next_state == "E":
            new_path = list.copy(path)
            new_path.append(new_pos)
            return new_path
        if next_state == ".":
            new_path = list.copy(path)
            new_path.append(new_pos)
            print(len(path), new_pos)
            return find_path(new_pos, new_path, grid)
    

mod_path = Path(__file__).parent
relative_path_1 = 'Day 20 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

grid = [list(i.strip()) for i in input_lines]
grid_height = len(grid)
grid_width = len(grid[0])
print(grid_height, grid_width)
def valid(pos):
    return 1 <= pos[0] < grid_height-1 and 1 <= pos[1] < grid_width-1

def find_n_away(n, pos):
    possible = []
    for i in range(n):
        new_pos = (pos[0]-i, pos[1]+n-i)
        if valid(new_pos):
            possible.append(new_pos)
        new_pos = (pos[0]+n-i, pos[1]+i)
        if valid(new_pos):
            possible.append(new_pos)
        new_pos = (pos[0]+i, pos[1]-n+i)
        if valid(new_pos):
            possible.append(new_pos)
        new_pos = (pos[0]-n+i, pos[1]-i)
        if valid(new_pos):
            possible.append(new_pos)
    return possible

start_pos = find_index("S", grid)
path = find_path(start_pos, [start_pos], grid)
at_least_100 = 0
old = time.time()
for ind, pos in enumerate(path):
    print(ind)
    for i in range(2, 21):
        if len(path)-ind-1 <= i:
            continue
        #ind+i < len(path)-1 -> i < len(path)-ind-1
        for after_cheat_pos in find_n_away(i, pos):
            if after_cheat_pos in path[100+ind+i:]:
                #path.index... - ind - i >= 100 -> path.index... >= 100 + ind + i
                at_least_100 += 1
print(time.time() - old)
print(at_least_100)



    