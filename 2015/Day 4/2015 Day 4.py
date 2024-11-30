from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path = '2015 Day 4 input.txt'
src_path = (mod_path / relative_path).resolve()
with open(src_path,"r") as _file:
    key = _file.read().strip()

import hashlib
def main(part1):
    i = 0
    while True:
        to_check = key + str(i)
        if hashlib.md5(to_check.encode('utf-8')).hexdigest()[:6-part1] == "0"*(6-part1):
            return i
        i += 1

print(main(False))