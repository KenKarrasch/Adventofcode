f = [i.split('-') for i in open('24-23.txt').read().split('\n')]

# Took some trawling on the internet to get a good algorithm for getting cliques in a population, Bron-Kerbosch, worked a treat.
# Needed to code a dictionary of interconnected links first.

cd = []
for i in range(len(f)):  # Get a list of unique computers
    for sd in [0,1]:
        if f[i][sd] not in cd:
            cd.append(f[i][sd])

cts = {}  # Dictionary of what each computer is connected to
for c in cd:
    cct = []
    for i in f:        
        for lr in [0,1]:
            if i[lr] == c:                
                cct.append(i[1-lr])
    cts[c] = cct

for k,v in cts.items():
    print(k,v)

from collections import defaultdict

def bron_kerbosch(graph):
    def bk_pivot(r, p, x, maximal):
        if not p and not x:
            if len(r) > len(maximal[0]):
                maximal[0] = r.copy()
            return
        
        pivot = max(p.union(x), key=lambda u: len(p.intersection(graph[u])))
        for v in p.difference(graph[pivot]):
            bk_pivot(r.union({v}), 
                     p.intersection(graph[v]), 
                     x.intersection(graph[v]),
                     maximal)
            p.remove(v)
            x.add(v)

    maximal = [set()]
    bk_pivot(set(), set(graph.keys()), set(), maximal)
    return list(maximal[0])

def largest_fully_connected_group(connections):
    # Convert connections to an undirected graph
    graph = defaultdict(set)
    for node, neighbors in connections.items():
        for neighbor in neighbors:
            graph[node].add(neighbor)
            graph[neighbor].add(node)
    
    return bron_kerbosch(graph)

largest_group = largest_fully_connected_group(cts)
largest_group.sort()
print(f"The largest fully connected group is: {largest_group}")
print(','.join(largest_group))
