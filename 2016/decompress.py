#example = "A(2x2)BCD(2x2)EFG"
#example = "A(1x5)BC"
example = "X(8x2)(3x3)ABCY"
example2 = "(27x12)(20x12)(13x14)(7x10)(1x12)A" 

def decomPressSymbol(string):
	print string
	i = 0
	length = 0
	while i < len(string):
		if string[i] == '(': 
			tmp = string[i+1:i+10].split('x')			
			length += int(tmp[0]) * int(tmp[1].split(')')[0])
			while i < len(string) and string[i] != ')':
				i += 1				
			i += int(tmp[0]) + 1
		else:
			i+=1
			length += 1
	return length 

def ParseSymbol(data,i):
	tmp = data[i+1:i+15].split('x')			
	a = tmp[0]
	b = tmp[1].split(')')[0]
	size = 3 + len(a) + len(b)
	return size,a,b

def Solve(data):
	i = 0
	length = 0
	print data
	while i < len(data):
		if data[i] == '(': 
			size,a,b = ParseSymbol(data,i)
			i += size + int(a)
			length += decomPressSymbol(data[i:i+int(a)*int(b)])
		else:
			i += 1
			length += 1
	return length

with open("day9_input") as f: 
	#print Solve(f.read())
	print Solve(example)
