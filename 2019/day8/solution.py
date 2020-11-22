N = 25
M = 6
layers = []
with open("input.txt") as f:
    input = f.readline()
    start = 0
    end = N*M
    while end <= len(input):
        layers.append(input[start:end])
        start = end 
        end = start + N*M

min = 999999999
minIndex = 0
for (index,layer) in enumerate(layers):
    count = layer.count('0')
    if count < min:
        min = count
        minIndex = index

minLayer = layers[minIndex]
print(minLayer.count('1')*minLayer.count('2'))