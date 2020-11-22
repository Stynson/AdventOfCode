from collections import defaultdict

graph = defaultdict(list)
with open("input.txt") as f:
    for line in f:
        data = line.strip().split(')')
        graph[data[1]].append(data[0])

graph = dict(graph) 

def traceKey(key):
    if key in graph:
        sum = 0
        for sub_key in graph[key]:
            sum += traceKey(sub_key) 
        return 1 + sum
    return 0
    
sum = 0
for key in graph:
    sum += traceKey(key)

print(sum)