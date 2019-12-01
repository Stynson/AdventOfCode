example1 = 'R2, R2, R2'
example2 = 'R5, L5, R5, R3'
example3 = 'R8, R4, R4, R8'
input = 'R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5'
	
def Generator(input):
	for i in input.split(', '):
		yield (i[0],int(i[1:]))

def Step(position,quarter,distance,steppedPositions):
	if quarter >= 2 :
			distance = -distance 
	index = 0
	if quarter % 2 == 0:
		index = 1 
	#print "new"
	if distance < 0:
		walkRange = range(position[index],position[index]+distance-1,-1)
	else:  
		walkRange = range(position[index],position[index]+distance+1)
	for i in walkRange:
		#print i 
		if index == 0:
			generatedPosition = [i,position[1]]
		else:
			generatedPosition = [position[0],i]
		steppedPositions.append(generatedPosition)
	position[index] += distance 
	#print position

#North = 0
#East = 1
#South = 2
#West = 3

def contains(small, big):
	for i in small:
		for j in big:
			if i == j:
				return i
	return False

def Solve():
	quarter = 0
	position = [0,0] 
	generator = Generator(input) 
	positions = []
	for direction,distance in generator:
		if direction == 'L':
			quarter = (quarter - 1) % 4
		else:
			quarter = (quarter + 1) % 4
		steppedPositions = []
		Step(position,quarter,distance,steppedPositions)
		result = contains(steppedPositions[1:],positions)
		if result:
			print "result: " + str(result)
			print abs(result[0]) + abs(result[1])
			break
		positions +=steppedPositions

	
Solve() 
