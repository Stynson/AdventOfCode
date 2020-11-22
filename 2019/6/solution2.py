from collections import defaultdict

graph = defaultdict(list)
with open("input.txt") as f:
#with open("testinput2.txt") as f:
    for line in f:
        data = line.strip().split(')')
        graph[data[1]].append(data[0])
        graph[data[0]].append(data[1])

graph = dict(graph) 

visited = []
def traceKey(key, sum):
    if key == "SAN": print(sum - 1)
    if key in graph and key not in visited:
        visited.append(key)
        for sub_key in graph[key]:
            traceKey(sub_key, sum + 1) 
    




traceKey(graph['YOU'][0], 0)