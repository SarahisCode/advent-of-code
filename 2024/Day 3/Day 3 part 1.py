from pathlib import Path
import re

mod_path = Path(__file__).parent
relative_path_1 = 'Day 3 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_stuff = a.read()

possible_muls = re.findall("mul\(([0-9]+),([0-9]+)\)", input_stuff)
print(possible_muls)
tot = 0
for pair in possible_muls:
    tot += int(pair[0])*int(pair[1])
print(tot)