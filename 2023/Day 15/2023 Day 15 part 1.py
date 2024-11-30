with open("C:/Users/willi/.vscode/Advent of Code/2023/Day 15/Day 15 input.txt", "r") as _file:
    instructions = _file.read().strip().split(",")
print(instructions)
_sum = 0
for instruction in instructions:
    curr = 0
    for char in instruction:
        curr += ord(char)
        curr *= 17
        curr %= 256
    _sum += curr
print(_sum)