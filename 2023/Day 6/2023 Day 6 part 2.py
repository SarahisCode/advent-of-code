from math import floor, ceil, sqrt

races = """Time:        41     66     72     66
Distance:   244   1047   1228   1040""".strip().split("\n")
time = 41667266
distance = 244104712281040
bottom = floor(time/2-sqrt((time/2)**2-distance))+1
top = ceil(time/2+sqrt((time/2)**2-distance))-1
print(top-bottom+1)