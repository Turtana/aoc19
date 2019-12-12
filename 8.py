width = 25
height = 6

with open("8.txt", "r") as file:
    data = file.read()

def printlayer(l):
    i = 0
    while True:
        print(l[i:i+width])
        i += width
        if i >= len(l):
            break

res = width*height
i = 0
layers = []
least0 = 999999
leastsum = 0
while True:
    layer = data[i:i+res]
    if layer.count("0") < least0:
        least0 = layer.count("0")
        leastsum = layer.count("1") * layer.count("2")
    layers.append(layer)
    i += res
    if i+res > len(data):
        break
print("Checksum:", leastsum)

finallayer = ""
for i in range(res):
    px = "2"
    for lay in layers:
        px = lay[i]
        if px != "2":
            finallayer += px
            break

finallayer = finallayer.replace("1", "#").replace("0", " ")
printlayer(finallayer)
        
