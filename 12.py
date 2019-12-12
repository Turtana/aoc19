from itertools import combinations

class Moon:
    def __init__(self, name, loc):
        self.loc = loc
        self.vel = [0,0,0]
        self.name = name
    def add_vel(self, vel):
        v = self.vel
        self.vel = [v[0] + vel[0], v[1] + vel[1], v[2] + vel[3]]
    def update_pos(self):
        self.loc = [self.loc[0] + self.vel[0], self.loc[1] + self.vel[1], self.loc[2] + self.vel[2]]

def gravitate(pair):
    for i in range(3):
        delta = 0
        if pair[0].loc[i] > pair[1].loc[i]:
            delta = 1
        elif pair[0].loc[i] < pair[1].loc[i]:
            delta = -1
        pair[0].vel[i] -= delta
        pair[1].vel[i] += delta

def calc_energy():
    total = 0
    for m in moons:
        total += sum(list(map(abs, m.loc))) * sum(list(map(abs, m.vel)))
    return total

states = []
x_stat = []
io = Moon("Io", [1,3,-11])
europa = Moon("Europa", [17,-10,-8])
ganymede = Moon("Ganymede", [-1,-15,2])
callisto = Moon("Callisto", [12,-4,-4])
moons = [io, europa, ganymede, callisto]

pairs = list(combinations(moons, 2))

steps = 100000
i = 0
while True:
##    print("\nSteps:", i+1)
    # Save the state
    
    x = []
    for moon in moons:
        x.extend([moon.loc[2], moon.vel[2]])
    if i == 0:
        x_stat = x
        
    for pair in pairs:
        gravitate(pair)
    for moon in moons:
        moon.update_pos()
##        print(moon.name, moon.loc, moon.vel)


    # FIRST check if the state is in previous states, THEN add it to previous states
##    if state in states:
##        print("An original state has returned! Steps taken:", i+1)
##        print("State:", state, "which was last seen in step", states.index(state))
##        break
    i += 1    
    
    if x == x_stat:
        if i != 1:
            print("y has repeated!", i)
            break

print("\nEnergy in the system:", calc_energy())
