def parse_opcode(opcode):
    op = str(opcode)
    if len(op) < 3:
        return [opcode]
    cmd = [int(op[-2:])]
    for i in range(len(op)+1):
        if i > 2:
            cmd.append(int(op[-i]))
    return cmd
# returns something like [2, 1, 0, 1]
# first is operand, others either 1, 2 or 0

with open("9.txt", "r") as file:
    code = file.read().split(",")
    code = list(map(int, code))


code.extend([0] * 32000) # MEMORY!!!
i = 0
rbase = 0
while True:
    step = 4
    cmd = parse_opcode(code[i])
    cmd.extend([0,0])
    
    a = code[i+1]
    if cmd[1] == 0:
        a = code[code[i+1]]
    elif cmd[1] == 2:
        a = code[code[i+1] + rbase]

    b = code[i+2]
    if cmd[2] == 0:
        b = code[code[i+2]]
    elif cmd[2] == 2:
        b = code[code[i+2] + rbase]

##    print(cmd[:-2], a, b)
    force_move = False

    if cmd[0] == 1:
        r = 0
        if cmd[3] == 2:
            r = rbase
        code[code[i+3] + r] = a + b
    elif cmd[0] == 2:
        r = 0
        if cmd[3] == 2:
            r = rbase
        code[code[i+3] + r] = a * b
    elif cmd[0] == 3:
        r = 0
        if cmd[1] == 2:
            r = rbase
        code[code[i+1] + r] = int(input("INPUT: "))
        step = 2
    elif cmd[0] == 4:
        print("OUTPUT:", a)
        step = 2
    elif cmd[0] == 5:
        step = 3
        if a != 0:
            i = b
        else:
            force_move = True
    elif cmd[0] == 6:
        step = 3
        if a == 0:
            i = b
        else:
            force_move = True
    elif cmd[0] == 7:
        r = 0
        if cmd[3] == 2:
            r = rbase
        code[code[i+3] + r] = 1 if a < b else 0
    elif cmd[0] == 8:
        r = 0
        if cmd[3] == 2:
            r = rbase
        code[code[i+3] + r] = 1 if a == b else 0
    elif cmd[0] == 9:
        rbase += a
        step = 2
    elif cmd[0] == 99:
        print("Program complete")
        break
    else:
        print("derp crash", cmd)
        break

    if (cmd[0] != 5 and cmd[0] != 6) or force_move:
        i += step
