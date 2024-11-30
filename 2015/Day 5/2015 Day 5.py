from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path = '2015 Day 5 input.txt'
src_path = (mod_path / relative_path).resolve()
with open(src_path,"r") as _file:
    strings = [i.strip() for i in _file.readlines()]

def main(part1):
    _sum = 0
    if part1:
        vowels = "aeiou"
        letters = "abcdefghijklmnopqrstuvwxyz"
        forbidden = ["ab", "cd", 'pq', "xy"]
        for string in strings:
            if sum(i in string for i in forbidden) == 0:
                if sum(string.count(i) for i in vowels) >= 3:
                    if sum(i*2 in string for i in letters) > 0:
                        _sum += 1
    else:
        pass#basically totally different from part 1
    return _sum

print(main(True))
            


    

