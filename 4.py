low = 278384
high = 824795

possibilities = 0
for i in range(low, high+1):
    nui = str(i)
    adj = False
    go_home = False
    prev_char = '0'
    for e in nui:
        if int(e) < int(prev_char):
            go_home = True
            break
        elif nui.count(e+e) == 1:
            if nui.count(e+e+e) == 0:
                adj = True
        prev_char = e
    if go_home or not adj:
        continue
    print(i)
    possibilities += 1
    
print("Total:", possibilities)
    
