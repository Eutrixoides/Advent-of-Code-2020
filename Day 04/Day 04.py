def fixformatting(data):
    passports = []
    currentPassport = {}
    for line in data: 
        if line == "": # Stack Overflow code
            passports.append(currentPassport)
            currentPassport = {}
        else:
            for item in line.split(" "):
                key, value = item.split(":")
                currentPassport[key] = value
    passports.append(currentPassport)
    return passports

def validate(passport):
    items = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
    for item in items:
        if item not in passport:
            return False
    return True

def validatept2(passport):
    if validate(passport) == False:
        return False
    if not(1920 <= int(passport["byr"]) <= 2002):
        return False
    if not(2010 <= int(passport["iyr"]) <= 2020):
        return False
    if not(2020 <= int(passport["eyr"]) <= 2030):
        return False
    if passport["hgt"][-2:] not in {"cm","in"}:
        return False
    if passport["hgt"][-2:] == "cm" and not 150 <= int(passport["hgt"][0:-2]) <= 193:
        return False
    if passport["hgt"][-2:] == "in" and not 59 <= int(passport["hgt"][0:-2]) <= 76:
        return False
    if passport["hcl"][0] != "#" or len(passport["hcl"]) != 7:
        return False
    for char in passport["hcl"][1:]:
        if char not in set("0123456789abcdef"):
            return False
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if len(passport["pid"]) != 9:
        return False
    for char in passport["pid"]:
        if char not in set("0123456789"):
            return False
    return True

def part1(passports):
    count = 0
    for passport in passports:
        if validate(passport) == True:
            count += 1
    return count

def part2(passports):
    count = 0
    for passport in passports:
        if validatept2(passport) == True:
            count += 1
    return count


file = open("input.txt")
data = []
for line in file:
    data.append(line.strip())
passports = fixformatting(data)
print(f"Sol 1: {part1(passports)}")
print(f"Sol 2: {part2(passports)}")