from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = 'Day 7 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

def find_possible(nums, result):
    if max(nums) > result:
        return False
    elif len(nums) == 1:
        return nums[0] == result
    else:
        new_nums = [nums[0]+nums[1]] + nums[2:]
        if find_possible(new_nums, result):
            return True
        new_nums = [nums[0]*nums[1]] + nums[2:]
        if find_possible(new_nums, result):
            return True
        return False

tot = 0
for line in input_lines:
    result, nums = line.strip().split(": ")
    nums = [int(i) for i in nums.split(" ")]
    result = int(result)
    tot += find_possible(nums, result)*result
print(tot)