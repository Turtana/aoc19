def crossing(line1, line2):
    if line1[0][0] == line1[1][0]:
        verti = line1
        horiz = line2
    else:
        verti = line2
        horiz = line1
    if horiz[0][0] < verti[0][0] and horiz[1][0] > verti[0][0]:
        if verti[0][1] < horiz[0][1] and verti[1][1] > horiz[0][1]:
            return [verti[0][0], horiz[0][1]]
    else:
        return None

def countstepsuntil(wire, point):
    totalsteps = 0
    loc = [0,0]
    for instruct in wire:
        c = instruct[0]
        steps = int(instruct[1:])
        if c == "U":
            if loc[0] == point[0] and loc[1] < point[1] and loc[1]+steps > point[1]:
                return totalsteps + point[1] - loc[1]
            loc = [loc[0], loc[1] + steps]
        elif c == "D":
            if loc[0] == point[0] and loc[1] > point[1] and loc[1]-steps < point[1]:
                return totalsteps - point[1] + loc[1]
            loc = [loc[0], loc[1] - steps]
        elif c == "R":
            if loc[1] == point[1] and loc[0] < point[0] and loc[0]+steps > point[0]:
                return totalsteps + point[0] - loc[0]
            loc = [loc[0] + steps, loc[1]]
        elif c == "L":
            if loc[1] == point[1] and loc[0] > point[0] and loc[0]-steps < point[0]:
                return totalsteps - point[0] + loc[0]
            loc = [loc[0] - steps, loc[1]]
        totalsteps += steps
    print("Point not found, you done goofed up")
    return 9999999999

with open("3_alt.txt", "r") as file:
    code = file.read().split("\n")
    nucode = []
    for wire in code:
        wire = wire.split(',')
        nucode.append(wire)

code = nucode
sections = []
initslashes = []

first = True
for wire in code:
    loc = [0,0]
    totalsteps = 0
    for instruct in wire:
        c = instruct[0]
        steps = int(instruct[1:])
        if first:
            if c == "U":
                initslashes.append([loc, [loc[0], loc[1] + steps]])
                loc = [loc[0], loc[1] + steps]
            elif c == "D":
                initslashes.append([[loc[0], loc[1] - steps], loc])
                loc = [loc[0], loc[1] - steps]
            elif c == "R":
                initslashes.append([loc, [loc[0] + steps, loc[1]]])
                loc = [loc[0] + steps, loc[1]]
            elif c == "L":
                initslashes.append([[loc[0] - steps, loc[1]], loc])
                loc = [loc[0] - steps, loc[1]]
        else:
            if c == "U":
                for s in initslashes:
                    cross = crossing([loc, [loc[0], loc[1] + steps]], s)
                    if cross:
                        cross.append(totalsteps + cross[1] - loc[1])
                        sections.append(cross)
                loc = [loc[0], loc[1] + steps]
            elif c == "D":
                for s in initslashes:
                    cross = crossing([[loc[0], loc[1] - steps], loc], s)
                    if cross:
                        cross.append(totalsteps + loc[1] - cross[1])
                        sections.append(cross)
                loc = [loc[0], loc[1] - steps]
            elif c == "R":
                for s in initslashes:
                    cross = crossing([loc, [loc[0] + steps, loc[1]]], s)
                    if cross:
                        cross.append(totalsteps + cross[0] - loc[0])
                        sections.append(cross)
                loc = [loc[0] + steps, loc[1]]
            elif c == "L":
                for s in initslashes:
                    cross = crossing([[loc[0] - steps, loc[1]], loc], s)
                    if cross:
                        cross.append(totalsteps + loc[0] - cross[0])
                        sections.append(cross)
                loc = [loc[0] - steps, loc[1]]
        totalsteps += steps
    print("Wire length:", totalsteps)
    first = False

print(sections)

least = 10000000
leastloc = [999,999]
mode = 1
for s in sections:
    if mode == 1:
        manhattan = abs(s[0]) + abs(s[1])
        if manhattan < least:
            least = manhattan
            leastloc = s
    else:
        dist = countstepsuntil(code[0], [s[0], s[1]]) + s[2]
        if dist < least:
            least = dist
            leastloc = [s[0], s[1]]
    
print("Nearest crossing:", leastloc, "with the distance of", least)



# HUOM! KAIKKI LINJAT MÄÄRITELTÄVÄ VASEN-OIKEA, ALAS-YLÖS!

