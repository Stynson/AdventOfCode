# Task 1
#sum = 0
#with open("input.txt") as f:
#    for line in f:
#        sum += int(int(line) / 3) - 2
#
#print(sum)

# Task 2

def calculate_fuel(weight):
    return  int(int(weight) / 3) - 2

sum = 0
with open("input.txt") as f:
    for line in f:
        newfuel = calculate_fuel(line)
        while newfuel > 0:
            sum += newfuel 
            newfuel = calculate_fuel(newfuel)

print(sum)

