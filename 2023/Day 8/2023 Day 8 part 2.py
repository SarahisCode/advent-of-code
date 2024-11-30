from math import lcm
with open("C:/Users/willi/.vscode/Advent of Code/2023/Day 8/2023 Day 8 input.txt", "r") as _file:
    lines = _file.readlines()
instructions = lines[0].strip()
l_r_chart = {}
for l_r_info in lines[2:]:
    home = l_r_info.strip().split(" = ")[0]
    left_right = l_r_info.strip().split(" = ")[1][1:-1].split(", ")
    l_r_chart[home] = left_right

current_list = []
for node in l_r_chart.keys():
    if node[-1] == "A":
        current_list.append(node)

time = 0
i = 0
start_list = list.copy(current_list)
loop_info = {}
while True:
    instruction = instructions[i]
    if instruction == "L":
        for _ind, node in enumerate(current_list):
            current_list[_ind] = l_r_chart[node][0]
    elif instruction == "R":
        for _ind, node in enumerate(current_list):
            current_list[_ind] = l_r_chart[node][1]
    else:
        exit(0)
    i += 1
    time += 1
    if i >= len(instructions):
        i -= len(instructions)
    for _ind, node in enumerate(current_list):
        if node[-1] == "Z": 
            start = start_list[_ind]
            print(loop_info)
            if start not in loop_info:
                loop_info[start] = {"start offset":time}
            elif "loop time" not in loop_info[start]:
                loop_info[start]["loop time"] = time-loop_info[start]["start offset"]
    if len(loop_info) == 6:
        for thing in loop_info:
            if len(loop_info[thing]) < 2:
                break
        else:
            break

answer = 1
for i in loop_info:
    answer = lcm(answer, loop_info[i]["loop time"])
print(answer)


