from itertools import permutations
from threading import Thread

class Amplifier:
    def __init__(self, phase):
        with open("7.txt", "r") as file:
            self.initcode = file.read().split(",")
            self.initcode.extend([0,0,0,0,0])
        self.reset(phase)
        
    def reset(self, phase):
        self.code = list(map(int, self.initcode))
        self.phase = phase
        self.input = -999
        self.output = -999
        self.finished = False

    def run(self):
##        print("RUNNING AMPLIFIER", self.phase)
        i = 0
        input_count = 0
        code = self.code
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
                if input_count == 0:
                    code[code[i+1]] = self.phase
##                    print("INIT INPUT " + str(self.phase))
                else:
                    while self.input == -999:
                        pass
                    code[code[i+1]] = self.input
                    self.input = -999
##                    print(str(self.phase) + " INPUT: " + str(code[code[i+1]]))
                step = 2
                input_count += 1
            elif cmd[0] == 4:
##                print(str(self.phase) + " OUTPUT: " + str(a))
                self.output = a
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
##                print(self.phase, "Program complete")
                self.finished = True
                break
            else:
                print(self.phase, "derp crash", cmd)
                break

            if (cmd[0] != 5 and cmd[0] != 6) or force_move:
                i += step

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

amplies = []
for i in range(5):
    amplies.append(Amplifier(0))

def test_run(signal):
    i = 0
    for a in amplies:
        a.reset(signal[i])
        i += 1
    
    in_signal = 0
    threads = []
    for a in amplies:
        threads.append(Thread(target=a.run).start())
    amplies[0].input = 0

    next_input = -999
    running_output = 0
    while True:
        break_count = 0
        for a in amplies:
            if next_input != -999:
                a.input = next_input
                next_input = -999
                
            if a.output != -999:
                next_input = a.output
                running_output = a.output
                a.output = -999
            if a.finished:
                break_count += 1
        if break_count == 5:
            break
        
    print("Result:", running_output)
    return running_output


signals = list(permutations([5,6,7,8,9]))

s = signals[0]

max_signal = 0
for s in signals:
    print("TESTING", s)
    new_signal = test_run(s)
    if new_signal > max_signal:
        max_signal = new_signal

print("HIGHEST POSSIBLE SIGNAL:", max_signal)





    
