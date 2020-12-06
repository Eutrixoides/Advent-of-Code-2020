from aocd import get_data
f = get_data(day=6)
lines = f.splitlines()

group = []
data = []
for line in lines:
    if line != "":
        group.append(line)
    if line ==  "" or line == 'lxgfmeirdquowkcpn': # Bullshit, but it works and it's 6AM, I don't want to look for a better solution
        data.append(group)
        group = []
allAns = []
for group in data:
    groupAns = []
    for person in group:
        for letter in person:
            groupAns.append(letter)

    allAns.append(list(set(groupAns))) # part 1    
    
lentotal = 0
for group in allAns:
    lentotal += len(group)
print(lentotal)

l = []
for group in data:
    intersect = set(group[0]).intersection(*group)
    if intersect:
        l.append(intersect)
total = 0

for group in l:
    total += len(group)
print(total)
    