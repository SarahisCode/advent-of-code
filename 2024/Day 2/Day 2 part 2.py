with open("Day 2 input.txt", "r") as a:
    input_lines = a.readlines()

reports = [[int(j) for j in i.strip().split(" ")] for i in input_lines]
print(reports)
working = 0
for report in reports:
    for index in range(len(report)):
        new_report = list.copy(report)
        new_report.pop(index)
        if new_report == sorted(new_report):
            if False not in map(lambda a:
         1<=a<=3, [new_report[i]-new_report[i-1] for i in range(1, len(new_report))]):
                working += 1
                break
        elif new_report == sorted(new_report, reverse=True):
            if False not in map(lambda a:
         1<=a<=3, [new_report[i-1]-new_report[i] for i in range(1, len(new_report))]):
                working += 1
                break
    
print(working)