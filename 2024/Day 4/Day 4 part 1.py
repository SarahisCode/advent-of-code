from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = 'Day 4 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
#relative pathing is hard
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

#diagonal
horizontal = [i.strip() for i in input_lines]
height = len(horizontal)
width = len(horizontal[0])
vertical = [[horizontal[j][i] for j in range(height)] for i in range(width)]
print(vertical)
tot = 0
to_find = "XMAS"
for i in horizontal:
    tot += i.count(to_find)
    tot += i.count(to_find[::-1])

for i in vertical:
    tot += "".join(i).count(to_find)
    tot += "".join(i).count(to_find[::-1])

for i in range(height-len(to_find)+1):
    for j in range(width-len(to_find)+1):
        to_look_at = [horizontal[i+k][j+k] for k in range(len(to_find))]
        if "".join(to_look_at) == to_find or "".join(to_look_at) == to_find[::-1]:
            tot += 1
        to_look_at = [horizontal[i+len(to_find)-k-1][j+k] for k in range(len(to_find))]
        if "".join(to_look_at) == to_find or "".join(to_look_at) == to_find[::-1]:
            tot += 1
print(tot)