from math import floor, ceil, sqrt

races = """Time:        41     66     72     66
Distance:   244   1047   1228   1040""".strip().split("\n")
times = races[0].split(": ")[1].split(" ")
while "" in times:
    times.remove("")
distances = races[1].split(": ")[1].split(" ")
while "" in distances:
    distances.remove("")
times, distances = [int(i) for i in times], [int(i) for i in distances]
base = 1
for time, distance in zip(times, distances):
    bottom = floor(time/2-sqrt((time/2)**2-distance))+1
    top = ceil(time/2+sqrt((time/2)**2-distance))-1
    base *= top-bottom+1
print(base)