from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path = '2015 Day 3 input.txt'
src_path = (mod_path / relative_path).resolve()
with open(src_path,"r") as _file:
    instructions = _file.read().strip()

def main(part1):
    visiteds = [{(0,0)}]*(2-part1)
    print(visiteds)
    currents = [[0,0]]
    if not part1:
        currents.append([0,0])
    ind = 0
    for instruction in instructions:
        print(currents)
        if instruction == "^":
            currents[ind][1] += 1
        elif instruction == ">":
            currents[ind][0] += 1
        elif instruction == "v":
            currents[ind][1] -= 1
        else:
            currents[ind][0] -= 1
        visiteds[ind].add(tuple(currents[ind]))
        ind += 1
        ind %= 2-part1
    if part1:
        return len(visiteds[0])
    else:
        return len(visiteds[0]|visiteds[1])

print(main(False))
            


