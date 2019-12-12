from math import atan2, sqrt

with open("10.txt", "r") as file:
    data = file.read().split("\n")

coords = []
ind_line = 0
for line in data:
    ind_char = 0
    for char in line:
        if char == "#":
            coords.append([ind_char, ind_line])
        ind_char += 1
    ind_line += 1

max_detect = 0
best_place = [0,0]
best_angles = []
print("Total:", len(coords))
for c in coords:
    detect = 0
    angles = []
    for other_c in coords:
        if other_c == c:
            continue
        angle = atan2((c[0] - other_c[0]), (c[1] - other_c[1]))
        if angle in angles:
            continue
        angles.append(angle)
        detect += 1
    if detect > max_detect:
        max_detect = detect
        best_place = c
        best_angles = angles
##    print("You can see", detect, "asteroids from", c)

print("The best place is", best_place, "with", max_detect, "detected asteroids")

pos_angles = []
neg_angles = []
for an in best_angles:
    if an > 0:
        pos_angles.append(an)
    else:
        neg_angles.append(an)
        # 0 is part of negatives
pos_angles.sort(reverse=True)
neg_angles.sort(reverse=True)
angles = neg_angles + pos_angles
# angles = lazer rotate program

def dist_sort(f):
    return abs(best_place[0] - f[0]) + abs(best_place[1] - f[1])


asteroid_list = {}
for an in angles:
    fit_steroids = []
    for c in coords:
        if c == best_place:
            continue
        if atan2((best_place[0] - c[0]), (best_place[1] - c[1])) == an:
            fit_steroids.append(c)

    fit_steroids.sort(key=dist_sort)
    asteroid_list[an] = fit_steroids

# At this point asteroid_list is a dictionary of angles in the rotating order,
# each of which has a list of asteroids in the vaporization order. Yay!

# GIANT LAZER TIME!
# the lists will be destroyed...

vapor_count = 0
while vapor_count < len(coords) - 1:
    newangles = []
    for an in angles:
        popped = asteroid_list[an].pop(0)
        vapor_count += 1
        print("Vaporized", popped, "and it was number", vapor_count)
        if asteroid_list[an]: # if list not empty
            newangles.append(an)
    angles = newangles
