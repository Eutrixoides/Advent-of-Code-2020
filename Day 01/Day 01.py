inputs = open("input.txt", "r")
strlist = inputs.read().splitlines()
intlist = [int(i) for i in strlist]

for i in intlist:
    for r in intlist:
        for x in intlist:
            if (i + r + x == 2020) and (i != r != x):
                print(f"Num 1 is {i}, num 2 is {r}, num 3 is {x}, them multiplied is {i*r*x}")
        
    

input()