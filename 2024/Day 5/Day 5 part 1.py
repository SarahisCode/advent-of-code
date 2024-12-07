from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = 'Day 5 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

break_point = input_lines.index("\n")
orderings = [input_lines[i].strip().split("|") for i in range(break_point)]
updates = [input_lines[i].strip().split(",") for i in range(break_point+1, len(input_lines))]
print(orderings, updates)
tot = 0
for update in updates:
    works = True
    for i in range(len(update)-1):
        if [update[i], update[i+1]] not in orderings:
            works = False
    if works:
        tot += int(update[int((len(update)-1)/2)])
print(tot)