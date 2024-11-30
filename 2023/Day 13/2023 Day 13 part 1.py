from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path = '2023 Day 13 input.txt'
src_path = (mod_path / relative_path).resolve()
with open(src_path,"r") as _file:
    patterns = [i.split("\n") for i in _file.read().strip().split("\n\n")]
from copy import deepcopy    
def find_reflection(pattern):
    for reflection_line in range(len(pattern)-1):
        reflection_row = reflection_line + 0.5
        for ind, line in enumerate(pattern):
            if 0 <= 2*reflection_row - ind < len(pattern):
                if line != pattern[int(2*reflection_row)-ind]:
                    break
        else:
            return (reflection_line + 1)*100
    else:
        columns = [[line[i] for line in pattern] for i in range(len(pattern[0]))]
        for reflection_line in range(len(columns)-1):
            reflection_row = reflection_line + 0.5
            for ind, line in enumerate(columns):
                if 0 <= 2*reflection_row - ind < len(columns):
                    if line != columns[int(2*reflection_row)-ind]:
                        break
            else:
                return reflection_line + 1
        return -1
def flip(char):
    if char == ".":
        return "#"
    elif char == "#":
        return "."
_sum = 0
for pattern in patterns:
    with_smudge = find_reflection(pattern)
    for y, line in enumerate(pattern):
        for x, char in enumerate(line):
            new_pattern = deepcopy(pattern)
            new_pattern[y] = new_pattern[y][:x] + flip(char) + new_pattern[y][x+1:]
            result = find_reflection(new_pattern)
            if result != -1 and result != with_smudge:
                for line in new_pattern:
                    print(line)
                print(x,y)
                print(result)
                _sum += result
                break
        else:
            continue
        break

print(_sum)
    
