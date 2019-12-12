file = open("1.txt", "r")
numbers = file.readlines()
file.close()

n = 1
fuels = []
for l in numbers:
    n = int(l.strip("\n"))
    modulefuel = int(n/3)-2
    print("Polttoaineen perusmäärä:", modulefuel)
    newfuel = modulefuel
    fuelfuel = 0
    while True:
        newfuel = int(newfuel/3)-2
        if newfuel < 1:
            break
        fuelfuel += newfuel
        print("Lisää löpöä:", newfuel)
    
    fuels.append(modulefuel + fuelfuel)
fuel = sum(fuels)
print("Yhteensä:", fuel)


    
