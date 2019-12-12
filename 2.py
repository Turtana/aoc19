with open("2.txt", "r") as file:
    code = file.read().split(",")
    code = list(map(int, code))
print(code)

i = 0
while True:
    if code[i] == 1:
        code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
    elif code[i] == 2:
        code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
    elif code[i] == 99:
        print("Program complete")
        break
    else:
        print("derp", code[i])
        break
    i += 4

print(code)
