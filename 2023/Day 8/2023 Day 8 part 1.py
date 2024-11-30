with open("C:/Users/willi/.vscode/Advent of Code/2023/Day 8/2023 Day 8 input.txt", "r") as _file:
    lines = _file.readlines()
instructions = lines[0].strip()
l_r_chart = {}
for l_r_info in lines[2:]:
    home = l_r_info.strip().split(" = ")[0]
    left_right = l_r_info.strip().split(" = ")[1][1:-1].split(", ")
    l_r_chart[home] = left_right

i = 0
current = "AAA"
while current != "ZZZ":
    instruction = instructions[i%len(instructions)]
    if instruction == "L":
        current = l_r_chart[current][0]
    else:
        current = l_r_chart[current][1]
    i += 1
print(i)


