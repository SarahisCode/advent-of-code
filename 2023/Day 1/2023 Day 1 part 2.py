

from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = '2023 Day 1 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

lines = [i.strip() for i in input_lines]

num_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
def find_cali(line):
    for ind, char in enumerate(line):
        if char in ("0","1","2","3","4","5","6","7","8","9"):
            return int(char)
        else:
            for num_name in num_dict.keys():
                if line[ind:ind+len(num_name)] == num_name:
                    return num_dict[num_name]
                
def find_cali_rev(line):
    for ind, char in enumerate(line):
        if char in ("0","1","2","3","4","5","6","7","8","9"):
            return int(char)
        else:
            for num_name in num_dict.keys():
                if line[ind:ind+len(num_name)] == num_name[::-1]:
                    return num_dict[num_name]

_sum = 0
for line in lines:
    _sum += 10*find_cali(line) + find_cali_rev(line[::-1])
print(_sum)