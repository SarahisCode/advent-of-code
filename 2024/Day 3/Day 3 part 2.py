from pathlib import Path
import re

mod_path = Path(__file__).parent
relative_path_1 = 'Day 3 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_stuff = a.read()

usable = [i.split("don't()")[0] for i in input_stuff.split("do()")]
tot = 0
for string in usable:
    possible_muls = re.findall(r"mul\(([0-9]+),([0-9]+)\)", string)
    for pair in possible_muls:
        tot += int(pair[0])*int(pair[1])
print(tot)