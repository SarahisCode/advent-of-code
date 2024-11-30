from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path_1 = '2023 Day 10 input.txt'
src_path_1 = (mod_path / relative_path_1).resolve()
with open(src_path_1,"r") as _file:
    lines = _file.readlines()
from enum import Enum
def opposite(direction):
    """Returns the opposite of a direction i.e. opposite(NORTH) -> SOUTH"""
    return (-direction[0], -direction[1])


NORTH = (0,-1)
EAST = (1,0)
SOUTH = (0,1)
WEST = (-1,0)

class Place():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pipe = lines[y][x]
    
    def __add__(self, direction):
        return Place(self.x + direction[0], self.y + direction[1])
    
    def __eq__(self, place):
        return self.x == place.x and self.y == place.y
    
def can_connect(place, direction):
    if (place+direction).pipe == ".":
        return False
    return opposite(direction) in linkages[(place+direction).pipe]

ALL_DIRECTIONS = (NORTH, EAST, SOUTH, WEST)
linkages = {"F":(EAST, SOUTH), "-":(EAST, WEST), "|":(NORTH, SOUTH), "7":(WEST, SOUTH), "L":(EAST, NORTH), "J":(WEST, NORTH)}
lines = [line.strip() for line in lines]
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            animal = Place(x,y)

animal_link = ()
for direction in ALL_DIRECTIONS:
    if can_connect(animal, direction):
        animal_link = direction
        break

distance = 1
current = animal + animal_link
current_direction = animal_link
while current.pipe != "S":
    current_links = linkages[current.pipe]
    for link in current_links:
        if link != opposite(current_direction):
            new_link = link
    current = current + new_link
    current_direction = new_link
    distance += 1
print(distance/2)

