from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path = '2015 Day 2 input.txt'
src_path = (mod_path / relative_path).resolve()
with open(src_path,"r") as _file:
    lines = [line.strip() for line in _file.readlines()]



from itertools import combinations
def main(part1):
    _sum = 0
    for line in lines:
        nums = [int(i) for i in line.split("x")]
        faces = [i[0]*i[1] for i in combinations(nums, 2)]
        if part1:
            _sum += 2*sum(faces)+min(faces)
        else:
            _sum += 2*sum(nums)-2*max(nums) + nums[0]*nums[1]*nums[2]
    return _sum

print(main(False))
