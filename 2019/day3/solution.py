#from collections import defaultdict
#
#intersections = []
#lines = defaultdict(lambda: defaultdict(int))
#directions = { "U" : [-1,0] ,"D" : [1,0] ,"L" : [0,-1] ,"R" : [0,1] }
#
#with open("input.txt") as f:
#    wire_id = 0
#    for line in f: 
#        x = 0
#        y = 0
#        wire_id += 1
#        for command in line.split(","):
#            direction = command[0]
#            steps = int(command[1:])
#            for i in range(steps):
#                x += directions[direction][0]
#                y += directions[direction][1]
#                if lines[x][y] == 0:
#                    lines[x][y] = wire_id
#                elif lines[x][y] != wire_id:
#                    intersections.append([x,y])
#
#print(min(abs(x) + abs(y) for [x,y] in intersections))

#for i in range(-10, 11):
#    for j in range(-10,11):
#        print(lines[i][j], end="")
#    print()

from collections import defaultdict

intersections = []
lines = defaultdict(lambda: defaultdict(list))
directions = { "U" : [-1,0] ,"D" : [1,0] ,"L" : [0,-1] ,"R" : [0,1] }

with open("input.txt") as f:
    wire_id = 0
    for line in f: 
        x = 0
        y = 0
        steps = 0
        wire_id += 1
        for command in line.split(","):
            direction = command[0]
            length = int(command[1:])
            for i in range(length):
                x += directions[direction][0]
                y += directions[direction][1]
                steps += 1
                if len(lines[x][y]) == 0:
                    lines[x][y] = [wire_id, steps]
                elif lines[x][y][0] != wire_id:
                    intersections.append([x,y, steps + lines[x][y][1]])

print(min(abs(x) + abs(y) for [x,y,_] in intersections))
print(min(x[2] for x in intersections))