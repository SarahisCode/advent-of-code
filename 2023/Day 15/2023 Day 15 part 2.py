with open("C:/Users/willi/.vscode/Advent of Code/2023/Day 15/2023 Day 15 input.txt", "r") as _file:
    instructions = _file.read().strip().split(",")
print(instructions)
_sum = 0

def hash(locator):
    curr = 0
    for char in locator:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr

boxes = {}
for instruction in instructions:
    if "-" in instruction:
        label = instruction[:-1]
        box = hash(label)
        to_delete = -1
        if box not in boxes:
            continue
        for ind, lens in enumerate(boxes[box]):
            if lens[0] == label:
                to_delete = ind
        if to_delete != -1:
            boxes[box].pop(to_delete)
    else:
        label = instruction[:-2]
        focal_length = int(instruction[-1])
        box = hash(label)
        in_box = False
        if box not in boxes:
            boxes[box] = [(label, focal_length)]
            continue
        print(boxes[box])
        for ind, lens in enumerate(boxes[box]):
            if lens[0] == label:
                to_delete = ind
                in_box = True
        if in_box:
            boxes[box][to_delete] = (label, focal_length)
        else:
            boxes[box].append((label, focal_length))

focusing_power = 0
for box_ind in boxes:
    box_num = box_ind + 1
    box = boxes[box_ind]
    for pos_ind, lens in enumerate(box):
        pos = pos_ind + 1
        focal_length = lens[1]
        focusing_power += box_num*pos*focal_length
print(focusing_power)
