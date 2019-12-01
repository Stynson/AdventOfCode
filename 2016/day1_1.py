example1 = 'R2, R2, R2'
example = 'R5, L5, R5, R3'
input = 'R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5'
	
def Generator(input):
	for i in input.split(', '):
		yield (i[0],int(i[1:]))

def Step(position,quarter,distance):
	if quarter >= 2 :
		distance = -distance
	index = 1
	if quarter % 2 == 0:
		index = 0 
	position[index] += distance 

#North = 0
#East = 1
#South = 2
#West = 3

def Solve():
	quarter = 0
	position = [0,0] 
	generator = Generator(input) 
	for direction,distance in generator:
		if direction == 'L':
			quarter = (quarter - 1) % 4
		else:
			quarter = (quarter + 1) % 4
		Step(position,quarter,distance)
	print abs(position[0]) + abs(position[1])
	
Solve() 
