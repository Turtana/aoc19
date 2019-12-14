import math

formulas = {}
test = '''2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF'''
with open("14.txt", "r") as file:
##    lines = file.read().split("\n")
    lines = test.split("\n")
    for l in lines:
        new = l.split(" => ")
        keyamount, key = new[1].split(" ")
        values = new[0].split(", ")
        newvalues = []
        for v in values:
            newvalues.append(v.split(" "))
        formulas[key] = [int(keyamount)] + newvalues

first_products = {}
def search_ingredients(amount, thing, endmode=False):
    if thing == "ORE":
##        print("Ore needed:", amount)
        return amount
    array = formulas[thing]
        
    cycles = math.ceil(amount / array[0]) # go round more if more is needed
    
##    print("Searching for", amount, thing, array, "Cycles:", cycles)
    ore_count = 0
    for i in range(cycles):
        for e in range(1, len(array)):
            if array[e][1] == "ORE":
                if i>0 and not endmode:
                    continue
                if thing in first_products:
                    first_products[thing] += amount
                else:
                    first_products[thing] = amount
##                print("+"+str(amount), thing, "needed")
            ore_count += search_ingredients(int(array[e][0]), array[e][1])
    if endmode:
        pass
##        print(ore_count)
    return ore_count
print("Originally:", search_ingredients(1, "FUEL"))
print(first_products)
fuel_needed = 0
leftovers = 0
for product in first_products:
    fuel_needed += search_ingredients(first_products[product], product, True)
print("Ore needed:", fuel_needed)
