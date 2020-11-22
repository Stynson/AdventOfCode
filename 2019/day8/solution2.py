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

image = layers[0]

for layer in layers:
    new_image = []
    for i in range(len(image)):
        if image[i] == '2':
            new_image.append(layer[i])
        else:
            new_image.append(image[i])
    image = "".join(new_image)


image = image.replace("0", ".")
image = image.replace("1", "o")
for i in range(M):
    print(image[i*N:i*N+N])