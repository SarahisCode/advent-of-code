from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path = '2023 Day 12 input.txt'
src_path = (mod_path / relative_path).resolve()
with open(src_path,"r") as _file:
    lines = [line.strip() for line in _file.readlines()]

from itertools import permutations

def works(conditions, record):
    current_group = 0
    in_group = False
    current_group_length = 0
    for char in conditions:
        if char == "#":
            if in_group:
                current_group_length += 1
            else:
                in_group = True
                current_group_length = 1
        elif char == "." and in_group:
            in_group = False
            if current_group >= len(record):
                return False
            elif not record[current_group] == current_group_length:
                return False
            current_group_length = 0
            current_group += 1
    if in_group:
        if current_group >= len(record):
            return False
        elif not record[current_group] == current_group_length:
            return False
        current_group += 1
    if current_group != len(record):
        return False
    return True


_sum = 0
for line in lines:
    conditions, record = line.split(" ")
    record = [int(i) for i in record.split(",")]
    num_unknown = conditions.count("?")
    possible = 0
    to_check = [""]
    for i in range(num_unknown):
        to_check = [j + "." for j in to_check] + [j+"#" for j in to_check]
    for possible_fill in to_check:
        new_conditions = []
        current_ind = 0
        for char in conditions:
            if char == "?":
                new_conditions.append(possible_fill[current_ind])
                current_ind += 1
            else:
                new_conditions.append(char)
        new_conditions = "".join(new_conditions)
        if works(new_conditions, record):
            possible += 1
    _sum += possible
print(_sum)

