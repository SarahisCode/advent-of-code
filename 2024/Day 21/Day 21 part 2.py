from pathlib import Path
from itertools import permutations, combinations

mod_path = Path(__file__).parent
relative_path_1 = 'Day 21 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

def find_index(thing, grid):
    for fpos, line in enumerate(grid):
        for spos, char in enumerate(line):
            if char == thing:
                return (fpos, spos)

def move(direction, position):
    if direction == "^":
        return (position[0]-1, position[1])
    elif direction == ">":
        return (position[0], position[1]+1)
    elif direction == "v":
        return (position[0]+1, position[1])
    elif direction == "<":
        return (position[0], position[1]-1)
    else:
        raise ValueError
    

def valid(start, moves, keypad):
    new_pos = start
    for direction in moves:
        new_pos = move(direction, new_pos)
        if keypad[new_pos[0]][new_pos[1]] == " ":
            return False
    return True

path_lookup = {}
def find_path(start, end, keypad):
    if start == end:
        return "A"
    if (start, end, keypad) in path_lookup.keys():
        return path_lookup[(start, end, keypad)]
    x_offset = end[0]-start[0]
    y_offset = end[1]-start[1]
    if x_offset > 0:
        x_moves = "v"*x_offset
    elif x_offset < 0:
        x_moves = "^"*(x_offset*-1)
    else:
        x_moves = ""
    if y_offset > 0:
        y_moves = ">"*y_offset
    elif y_offset < 0:
        y_moves = "<"*(y_offset*-1)#has to be positive
    elif y_offset == 0:
        y_moves = ""
    if x_moves == "" or y_moves == "":
        possible = [x_moves+y_moves]
    else:
        if y_offset < 0 and valid(start, y_moves+x_moves, keypad):
            return y_moves+x_moves
        else:
            possible = [x_moves+y_moves, y_moves+x_moves]#assumption

    new_possible = []
    for route in possible:
        if valid(start, route, keypad):
            new_possible.append("".join(route)+"A")
    path_lookup[(start, end, keypad)] = new_possible[0]
    return new_possible[0]


num_keypad = ("789", "456", "123", " 0A")
dir_keypad = (" ^A", "<v>")
num_positions = {}
dir_positions = {}
for i in "0123456789A":
    num_positions[i] = find_index(i, num_keypad)
for i in "<^>vA":
    dir_positions[i] = find_index(i, dir_keypad)
ans = 0
for line in input_lines:
    current_moves = []
    to_visit_names = "A"+line.strip()#adding A because the robot starts at A
    to_visit_positions = [find_index(i, num_keypad) for i in to_visit_names]
    path = ""
    for pointer in range(len(to_visit_positions)-1):
        start = to_visit_positions[pointer]
        end = to_visit_positions[pointer+1]
        to_add = find_path(start, end, num_keypad)
        path = path + to_add
    for i in range(25):
        print(i, len(path))
        all_path_choices = []
        prev_layer_path = path
        to_visit_names = "A"+prev_layer_path#adding A because the robot starts at A
        to_visit_positions = [dir_positions[i] for i in to_visit_names]
        this_path = ""
        for pointer in range(len(to_visit_positions)-1):
            start = to_visit_positions[pointer]
            end = to_visit_positions[pointer+1]
            to_add = find_path(start, end, dir_keypad)
            this_path = this_path+to_add
        path = this_path
    min_len = len(path)
    to_enter_num = int(line.strip()[:-1])
    to_add = to_enter_num*min_len
    ans += to_add
print(ans)

