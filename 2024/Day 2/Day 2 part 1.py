from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = 'Day 2 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1, "r") as a:
    input_lines = a.readlines()

reports = [[int(j) for j in i.strip().split(" ")] for i in input_lines]
print(reports)
working = 0
for report in reports:

    if report == sorted(report):
        if False not in map(lambda a:
         1<=a<=3, [report[i]-report[i-1] for i in range(1, len(report))]):
            working += 1
    elif report == sorted(report, reverse=True):
        if False not in map(lambda a:
         1<=a<=3, [report[i-1]-report[i] for i in range(1, len(report))]):
            working += 1
    
print(working)