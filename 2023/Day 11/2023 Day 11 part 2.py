from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path_1 = '2023 Day 11 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1,"r") as _file:
    lines = [line.strip() for line in _file.readlines()]

from itertools import combinations
from math import fabs
empty_rows = []
empty_columns = []
for ind, row in enumerate(lines):
    if "#" not in row:
        empty_rows.append(ind)

for ind in range(len(lines[0])):
    for row in lines:
        if row[ind] == "#":
            break
    else:
        empty_columns.append(ind)

galaxies = []
for y, row in enumerate(lines):
    for x, char in enumerate(row):
        if char == "#":
            galaxies.append((x,y))

to_check = combinations(galaxies, 2)

_sum = 0
for pair in to_check:
    galaxy_1 = pair[0]
    galaxy_2 = pair[1]
    distance = fabs(galaxy_1[0]-galaxy_2[0]) + fabs(galaxy_1[1]-galaxy_2[1])
    for column in range(min(galaxy_1[0], galaxy_2[0])+1, max(galaxy_1[0], galaxy_2[0])):
        if column in empty_columns:
            distance += 999999
    for row in range(min(galaxy_1[1], galaxy_2[1])+1, max(galaxy_1[1], galaxy_2[1])):
        if row in empty_rows:
            distance += 999999
    _sum += distance

print(_sum)


