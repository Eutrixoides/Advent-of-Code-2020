import collections
import re
from aocd import get_data
f = get_data(day=7)
lines = f.splitlines()

colorIsInside = collections.defaultdict(set) # Defaultdict doesn't give me keyerror
colorHasInside = collections.defaultdict(list)
    
for line in lines:
    color = line.split(' bags contain')[0]
    for num, colorinbag in re.findall(r'(\d+) (.+?) bags?[,.]', line): # Regex ruined my day, but idk how to do it without regex
        num = int(num)
        colorIsInside[colorinbag].add(color)
        colorHasInside[color].append((num, colorinbag))

# part 1:
hasshinygold = set()
def check(color = 'shiny gold'):
    for c in colorIsInside[color]:
        hasshinygold.add(c)
        check(c)
    return len(hasshinygold)
print(check())


def cost(color = 'shiny gold'):
    total = 0
    for  num,inner in colorHasInside[color]:
        total += num
        total += num * cost(inner)
    return total
print(cost())
