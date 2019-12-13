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

def draw():
    screen = "\nSCORE: " + str(score)
    for y in range(24):
        screen += "\n"
        for x in range(42):
            screen += pixels[(x,y)]
    print(screen)

with open("13.txt", "r") as file:
    code = file.read().split(",")
    code = list(map(int, code))


code.extend([0] * 32000) # MEMORY!!!
i = 0
rbase = 0

ball_x = 0
paddle_x = 0

out_index = 0
pixels = {}
pix = [0,0," "]
score = 0
while True:
    step = 4
    cmd = parse_opcode(code[i])
    cmd.extend([0,0,0])
    
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
        draw()
        r = 0
        if cmd[1] == 2:
            r = rbase
##        inp = int(input("INPUT: "))
        inp = 0
        if paddle_x < ball_x:
            inp = 1
        elif paddle_x > ball_x:
            inp = -1
        code[code[i+1] + r] = inp
        step = 2
    elif cmd[0] == 4:
        if out_index == 2:
            if pix[:2] == [-1, 0]:
##                print("SCORE:", a)
                score = a
            if a == 0:
                pix[2] = " "
            elif a == 1:
                pix[2] = "X"
            elif a == 2:
                pix[2] = "#"
            elif a == 3:
                pix[2] = "="
                paddle_x = pix[0]
            elif a == 4:
                pix[2] = "o"
                ball_x = pix[0]
            pixels[(pix[0], pix[1])] = pix[2]
            pix = [0,0," "]
            out_index = 0
        else:
            pix[out_index] = a
            out_index += 1
##        print("OUTPUT:", a)
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

