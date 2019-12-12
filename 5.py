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
# first is operand, others either 1 or 0

with open("5.txt", "r") as file:
    code = file.read().split(",")
    code = list(map(int, code))

code.extend([0,0,0,0,0])
i = 0
while True:
    step = 4
    cmd = parse_opcode(code[i])
    cmd.extend([0,0])
    if len(code) > code[i+1]:
        a = code[i+1] if cmd[1] else code[code[i+1]]
    if len(code) > code[i+2]:
        b = code[i+2] if cmd[2] else code[code[i+2]]
    force_move = False
    
    if cmd[0] == 1:
        code[code[i+3]] = a + b
    elif cmd[0] == 2:
        code[code[i+3]] = a * b
    elif cmd[0] == 3:
        code[code[i+1]] = int(input("INPUT: "))
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
        code[code[i+3]] = 1 if a < b else 0
    elif cmd[0] == 8:
        code[code[i+3]] = 1 if a == b else 0
    elif cmd[0] == 99:
        print("Program complete")
        break
    else:
        print("derp crash", cmd)
        break

    if (cmd[0] != 5 and cmd[0] != 6) or force_move:
        i += step
