import numpy as np
import os
import networkx as nx
import queue

def read_input():
    f = open('input2.txt').readlines()
    pos = 0j
    dict_map = {}
    keys = {}
    player = None
    for l in f:
        npos = pos
        for a in l:
            if a not in ['#','\n']:
                dict_map[pos] = a
            if a == '@':
                player = pos
                dict_map[pos] = '.'
            else:
                keys[a] = pos
            pos += 1
        pos = npos + 1j
    dimx = int(pos.real)
    dimy = int(pos.imag)
    
    return dict_map, player, keys

G = nx.Graph()
dict_map, player, keys = read_input()
for p in dict_map:
    for d in [-1, 1j, 1, -1j]:
        if (p+d) in dict_map:
            G.add_edge(p, p+d)

nx.set_node_attributes(G, dict_map, 'val')

# l = list(nx.bfs_edges(G, player))
# l = list(nx.bfs_tree(G, player))
# l = list(nx.dfs_preorder_nodes(G, player))

lower = {k:keys[k] for k in keys if k.islower()}
upper = {k:keys[k] for k in keys if k.isupper()}

print(lower)
print(upper)
paths = {}
for a in lower:
    print(a, a.upper())
    A = a.upper()
    if A in upper:
        l = list(nx.all_shortest_paths(G, lower[a], upper[a.upper()]))
        paths[a] = l
    print(l)

ll = list(nx.all_shortest_paths(G, player, [lower[k] for k in paths]))
print(ll)

exit(1)


q = [(player, 0, None)]
visited = []
_keys = {}
_doors = {}
while len(q)>0:
    node, dst, key = q.pop()
    if node not in visited:
        visited.append(node)
        if node['val'].isupper():
            if key is not None and node['val'] == key['val'].upper():
                node['val'] = '.'
                key['val'] = '.'
                continue
        elif node['val'].islower():
            key = node
        for n in G.neighbors(node):
            q.append([n, dst+1, key])




