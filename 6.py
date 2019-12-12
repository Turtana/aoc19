with open("6.txt") as file:
    orbits = file.read().split("\n")

orbitdata = {}

for orbit in orbits:
    data = orbit.split(")")
    orbitdata[data[1]] = data[0]

total = 0
for p in orbitdata:
    temp = p
    total += 1
    while orbitdata[temp] in orbitdata:
        total += 1
        temp = orbitdata[temp]
print("In total the system has", total, "orbits")

you_orbits = ["YOU"]
san_orbits = ["SAN"]

temp = "YOU"
while orbitdata[temp] in orbitdata:
    temp = orbitdata[temp]
    you_orbits.append(temp)
temp = "SAN"
while orbitdata[temp] in orbitdata:
    temp = orbitdata[temp]
    san_orbits.append(temp)

for p in you_orbits:
    if p in san_orbits:
        print("The closest planet is", p)
        ans = you_orbits.index(p) + san_orbits.index(p) - 2
        break

print("The shortest distance is", ans)

