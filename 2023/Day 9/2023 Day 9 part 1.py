with open("C:/Users/willi/.vscode/Advent of Code/2023 Day 9 input.txt", "r") as _file:
    lines = _file.readlines()
_sum = 0
for line in lines:
    values = [int(i) for i in line.strip().split(" ")]
    diffs = [list.copy(values)]
    while len(set(diffs[-1])) > 1:
        old_diff = diffs[-1]
        new_diff = []
        for i in range(len(old_diff)-1):
            new_diff.append(old_diff[i+1]-old_diff[i])
        diffs.append(new_diff)
    diffs[-1].append(diffs[-1][0])
    to_check = diffs[::-1]
    for ind, diff in enumerate(to_check):
        if ind == 0:
            continue
        to_check[ind].append(diff[-1]+to_check[ind-1][-1])
    _sum += diffs[0][-1]
print(_sum)