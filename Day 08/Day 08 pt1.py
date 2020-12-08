from aocd import get_data
f = get_data(day=8)
lines = f.splitlines()

instructions = []
for line in lines:
	code, value = line.split(" ")
	instructions.append([code,int(value)])

accumulator = 0
i = 0
norepeatlist = []

while True:
	if i in norepeatlist:
		break
	norepeatlist.append(i)
	
	if instructions[i][0] == "acc":
		accumulator += instructions[i][1]
	elif instructions[i][0] == "jmp":
		i += instructions[i][1] - 1	 
	i+=1

print(accumulator)