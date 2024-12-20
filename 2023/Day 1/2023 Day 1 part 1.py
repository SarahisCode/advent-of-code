def find_cali(line):
    for i in line:
        if i in ("0","1","2","3","4","5","6","7","8","9"):
            return int(i)

from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = '2023 Day 1 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

lines = [i.strip() for i in input_lines]
_sum = 0
for line in lines:
    _sum += 10*find_cali(line) + find_cali(line[::-1])
print(_sum)