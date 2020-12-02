def checkpassw(passw,slovo,min,max):
    slovoputaubroju = 0
    for i in passw:
        if i==slovo:
            slovoputaubroju+=1
    return (min <= slovoputaubroju <= max)


def part2passwcheck(passw, slovo, min, max):
    return (passw[min - 1] == slovo) != (passw[max - 1] == slovo) #Boolean true ili false je output


passwlistlist = []

input = open("input.txt", "r")
input2 = input.readlines()
for item in input2:
    rules,passw = item.split(': ')
    passw = passw[0:-1]
    #print(rules)
    brojevi,slovo = rules.split(' ')
    #print(brojevi)
    min,max = brojevi.split('-')
    passwlistlist.append([passw, slovo, int(min), int(max)])
    #print(rules,passw,slovo,min,max)
#print(passwlistlist)

checkpassnum = 0
part2num = 0
#Prvi dio zadatka
for passwlist in passwlistlist:
    if checkpassw(*passwlist) == True:
        checkpassnum +=1

#Drugi dio zadatka
for passwlist in passwlistlist:
    if part2passwcheck(*passwlist) == True:
        part2num += 1
    

print(f"Sol 1: {checkpassnum}")
print(f"Sol 2: {part2num}")


