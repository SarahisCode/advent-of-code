def valid(coord):
    return 0 <= coord <= len(lines)

with open("2023 Day 21 input.txt", "r") as _file:
    lines = _file.readlines()
possibilities = []
new_possibilities = []
for y, i in enumerate(lines):
    for x, j in enumerate(i):
        if j == "S":
            possibilities.append((x,y))
for i in range(64):
    for point in possibilities:
        for new_point in ((point[0]+1, point[1]), (point[0]-1, point[1]), (point[0], point[1]+1), (point[0], point[1]-1)):
            if valid(new_point[0]) and valid(new_point[1]) and lines[new_point[1]][new_point[0]] == "." and new_point not in new_possibilities:
                new_possibilities.append(new_point)
    possibilities, new_possibilities = list.copy(new_possibilities), []
print(len(possibilities))
print((65, 65) in possibilities)
