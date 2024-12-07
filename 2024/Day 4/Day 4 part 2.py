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
tot = 0
to_find = "MAS"
for i in range(height-len(to_find)+1):
    for j in range(width-len(to_find)+1):
        down_diag = "".join([horizontal[i+k][j+k] for k in range(len(to_find))])
        up_diag = "".join(horizontal[i+len(to_find)-k-1][j+k] for k in range(len(to_find)))
        if (down_diag == to_find or down_diag == to_find[::-1]) and (up_diag == to_find or up_diag == to_find[::-1]):
            tot += 1
print(tot)