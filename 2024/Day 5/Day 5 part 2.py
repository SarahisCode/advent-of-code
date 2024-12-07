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
    if not works:
        old_update = list.copy(update)
        cor_update = []
        while len(old_update) > 0:
            to_remove = []
            for i in old_update:
                to_add = True
                for j in old_update:
                    if j != i:
                        if [j,i] in orderings:
                            to_add = False
                if to_add:
                    cor_update.append(i)
                    to_remove.append(i)
                    break
            for i in to_remove:
                old_update.remove(i)
        print(cor_update)
        tot += int(cor_update[int((len(cor_update)-1)/2)])
print(tot)