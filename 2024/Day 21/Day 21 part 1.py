from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = 'Day 21 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

