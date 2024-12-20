from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = 'Day 8 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

grid = [i.strip() for i in input_lines]
