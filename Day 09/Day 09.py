from aocd import get_data
f = get_data(day=9)
lines = f.splitlines()
numbers = [int(line) for line in lines]

for i in range(25,len(numbers)):
	numsbefore = set(numbers[i-25:i])
	valid = False
	for item in range(i-25,i):
		if numbers[i]-numbers[item] in numsbefore:
			valid = True
			break
	if not valid:
		print(sol1:=numbers[i])

for startnum in range(len(numbers)):
	sum = 0
	j = 0
	while sum < sol1:
		sum += numbers[startnum+j]
		j+=1
	if sum==sol1 and j>1:
		sol2 = [numbers[x] for x in range(startnum,startnum+j)]
		print(min(sol2)+max(sol2))