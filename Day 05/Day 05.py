inputs = open("input.txt")
strlist = inputs.read().splitlines()
seatidlist = []
for string in strlist:
    fb = string[:7]
    rl = string[7:]
    fb = fb.replace('F','0')
    fb = fb.replace('B','1')
    fbint = int(fb,2)
    #print(fbint)
    rl = rl.replace('R','1')
    rl = rl.replace('L','0')
    rlint = int(rl,2)
    #print(rlint)
    seatid = fbint*8 + rlint
    #print(seatid)
    seatidlist.append(seatid)
print(f"Max is {max(seatidlist)}")

for seatid in range(min(seatidlist),max(seatidlist)):
    if seatid not in seatidlist:
        print(f'Your seat ID: {seatid}')
    
