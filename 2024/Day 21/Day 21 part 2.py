from pathlib import Path
from copy import deepcopy

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

#what the heck why are there 3 layers


#the can't go over empty space condition is problematic
#since it kind of screws up our possiblities
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

def find_paths(start, end, keypad):
    if start == end:
        return ["A"]
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
        possibilities = [x_moves+y_moves]
    else:
        possibilities = [x_moves+y_moves, y_moves+x_moves]
    new_possiblities = []
    for route in possibilities:
        if valid(start, route, keypad):
            new_possiblities.append(route+"A")
    return new_possiblities


num_keypad = ["789", "456", "123", " 0A"]
dir_keypad = [" ^A", "<v>"]
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
    path_choices = [""]
    for pointer in range(len(to_visit_positions)-1):
        start = to_visit_positions[pointer]
        end = to_visit_positions[pointer+1]
        to_add = find_paths(start, end, num_keypad)
        new_path_choices = []
        for add_path in to_add:
            for path in path_choices:
                new_path_choices.append(path + add_path)
        path_choices = deepcopy(new_path_choices)
    for _ in range(25):
        all_path_choices = []
        for prev_layer_path in path_choices:
            to_visit_names = "A"+prev_layer_path#adding A because the robot starts at A
            to_visit_positions = [find_index(i, dir_keypad) for i in to_visit_names]
            this_path_choices = [""]
            for pointer in range(len(to_visit_positions)-1):
                start = to_visit_positions[pointer]
                end = to_visit_positions[pointer+1]
                to_add = find_paths(start, end, dir_keypad)
                new_path_choices = []
                for add_path in to_add:
                    for path in this_path_choices:
                        new_path_choices.append(path + add_path)
                this_path_choices = deepcopy(new_path_choices)
            all_path_choices = all_path_choices + path_choices
        path_choices = deepcopy(all_path_choices)
        print([len(path) for path in path_choices])
        
    min_len = min(len(path) for path in path_choices)
    to_enter_num = int(line.strip()[:-1])
    to_add = to_enter_num*min_len
    ans += to_add
    #only 456A is wrong, but I don't know why
    #I dunno why they're all the same length
    #test time
    #trying to figure out how to do 0th+0th, 0th+1st, ...
#part 2 is going to suck, unless its "oh, there's a hundred directional pads"
#then my code hopefully won't explode
#maybe they'll change the layout?
print(ans)

