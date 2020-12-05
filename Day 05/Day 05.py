inputs = open("input.txt")
strlist = inputs.read().splitlines()
seatidlist = []
for string in strlist:
    fb, rl = string[:7], string[7:]
    fb = fb.replace('F','0').replace('B','1')
    rl = rl.replace('R','1').replace('L','0')
    fbint, rlint = int(fb,2), int(rl,2)
    seatid = fbint*8 + rlint
    seatidlist.append(seatid)

# Part 1
print(f"Max is {max(seatidlist)}")

# Part 2
for seatid in range(min(seatidlist),max(seatidlist)):
    if seatid not in seatidlist:
        print(f'Your seat ID: {seatid}')
    
