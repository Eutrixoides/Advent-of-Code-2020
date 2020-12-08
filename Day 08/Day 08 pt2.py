from aocd import get_data
f = get_data(day=8)
lines = f.splitlines()

instructions = []
for line in lines:
    code, value = line.split(" ")
    instructions.append([code, int(value)])

def solve(instructions):
    accumulator = 0
    i = 0
    seen = set()

    while i < len(instructions):
        instruction = instructions[i]
        code = instruction[0]
        value = instruction[1]

        if i in seen:
            return None

        seen.add(i)
        if code == "acc":
            accumulator += value
            i += 1
        elif code == "jmp":
            i += value
        elif code == "nop":
            i += 1

    return accumulator

for i, item in enumerate(instructions):
    flipped = None
    value = item[1]
    if item[0] == "jmp":
        flipped = "nop"
    elif item[0] == "nop":
        flipped = "jmp"
    else:
        continue

    copy = instructions[::]
    copy[i] = [flipped,value]
    
    if solve(copy) is not None:
        print(solve(copy))
        break
