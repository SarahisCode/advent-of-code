from helpers import *
from copy import deepcopy
with open("Day 1 input.txt", "r") as a:
    input_lines = a.readlines()
input_lines = [i.strip().split("   ") for i in input_lines]
print(input_lines)
list_1 = [int(i[0]) for i in input_lines]
list_2 = [int(i[1]) for i in input_lines]
list_1.sort()
list_2.sort()
print(sum(abs(list_1[i]-list_2[i]) for i in range(len(list_1))))