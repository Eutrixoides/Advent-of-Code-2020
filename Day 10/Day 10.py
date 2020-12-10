from aocd import get_data
f = get_data(day=10)
numbers = [int(line) for line in f.splitlines()]
numbers.append(0)
numbers = sorted(numbers)

# Part 1
jolt1 = jolt3 = 0
for i in range(1,len(numbers)):
	if numbers[i] == numbers[i-1] + 1:
		jolt1 += 1
	elif numbers[i] == numbers[i-1] + 3:
		jolt3 += 1
print(jolt1*(jolt3+1))

# Part 2
numbers.append(max(numbers) + 3)
idk = {}

def solutions(v = 0):
	if v in idk:
		return idk[v]
	if v == numbers[-1]: 
		return 1
	ans = 0
	if v+1 in numbers:
		ans += solutions(v+1)
	if v+2 in numbers:
		ans += solutions(v+2)
	if v+3 in numbers:
		ans += solutions(v+3)
	idk[v] = ans
	return idk[v]

print(solutions())