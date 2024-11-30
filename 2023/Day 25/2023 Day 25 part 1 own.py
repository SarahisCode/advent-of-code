from pathlib import Path
cwd = Path.cwd()
mod_path = Path(__file__).parent
relative_path = '2023 Day 25 input.txt'
src_path = (mod_path / relative_path).resolve()
with open(src_path,"r") as _file:
    lines = [line.strip() for line in _file.readlines()]


def traverse(connections, comp):
    current = []
    for i in all_comps:
        for j in current:
            if i not in j:
                break
    else:
        return 

    for i in connections[comp]:
        current = current + [j.append(i) for j in traverse(connections, i)]
    return current

connections = {}
for line in lines:
    comp, connect = line.split(": ")
    connect = connect.split(" ")
    if comp in connections:
        connections[comp] = connections[comp] + connect
    else:
        connections[comp] = connect
    for i in connect:
        if i in connections.keys():
            connections[i] = connections[i] + [comp]
        else:
            connections[i] = [comp]
for i in connections:
    print(len(connections[i]))
all_comps = connections.keys()

comp_paths = traverse(connections, comp)
print(comp_paths)
