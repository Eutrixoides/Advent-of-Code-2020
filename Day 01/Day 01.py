inputs = open("input.txt", "r")
strlist = inputs.read().splitlines()
intlist = [int(i) for i in strlist]

for i in intlist:
    for j in intlist:
        if i + j == 2020 and i != j:
            num1 = i
            num2 = j
            solution1 = i*j
        for k in intlist:
            if i + j + k == 2020 and i != j != k:
                sol2num1 = i
                sol2num2 = j
                sol2num3 = k
                solution2 = i * j * k

#First Star
print(f"Num 1 is {num1}, num 2 is {num2}, the solution for the first star is: {solution1}")

#Second Star
print(f"Num 1 is {sol2num1}, num 2 is {sol2num2}, num 3 is {sol2num3}, the solution for the second star is: {solution2}")

input()