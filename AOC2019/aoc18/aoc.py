import numpy as np
import os
import networkx as nx
import queue
from copy import deepcopy
from heapq import heappop, heappush

def read_input():
    with open('input.txt') as f:
        f = [x.strip() for x in f.readlines()]
        keys = {}
        G = nx.grid_2d_graph(len(f), len(f[0]), create_using=nx.Graph)
        for x in range(len(f)):
            for y in range(len(f[0])):
                if f[x][y] in ['#','\n']:
                    G.remove_node((x, y))
                elif f[x][y] == '@':
                    player = (x,y)
                    G.nodes[(x,y)]['val'] = '.'
                else:
                    if f[x][y].islower():
                        keys[f[x][y]] = (x,y)
                    G.nodes[(x,y)]['val'] = f[x][y]
        return G, player, keys
G, player, keys = read_input()

keys_all = [keys[k] for k in keys if k.islower()]

def get_doors(g, l):
    doors = set()
    for a in l:
        if g.nodes[a]['val'].isupper():
            doors.add(g.nodes[a]['val'].lower())
    return doors

if __name__== "__main__":
    graph = G
    # get all shortest paths with doors
    print('shortest path ....')
    shortest_path = {}
    for key_pos_a in [player] + keys_all:
        for key_pos_b in [player] + keys_all:
            if key_pos_a != key_pos_b:
                # print('doing ', graph.nodes[key_pos_a]['val'], graph.nodes[key_pos_b]['val'])
                id = (key_pos_b, key_pos_a)
                if id in shortest_path:
                    shortest_path[(key_pos_a, key_pos_b)] = shortest_path[id].copy()
                else:
                    node_to_key = list(nx.shortest_path(graph, key_pos_a, key_pos_b))
                    doors = get_doors(graph, node_to_key)
                    shortest_path[(key_pos_a, key_pos_b)] = [len(node_to_key)-1, doors]

    print('shortest path done!')
    node = player
    q = [(0, tuple(keys_all), set([]), player)]
    num_keys = len(keys_all)
    min_dst = 100000000000000

    visited = set()
    while True:
        dst, keys_left, keys_collected, node = heappop(q)
        id = (tuple(keys_left), ''.join(keys_collected))
        if id in visited:
            continue
        visited.add(id)
        # print('DEBUG: ', len(keys_left), len(keys_collected), num_keys, dst)
        if len(keys_collected)==num_keys:
            if dst < min_dst:
                min_dst = dst
                print(''.join(keys_collected))
                print(min_dst)
                break
        for key_pos in keys_left:
            if key_pos != node:
                id = (node, key_pos)
                lpath, doors = shortest_path[id]
                new_length = lpath + dst
                new_doors = doors - keys_collected
                if len(new_doors) == 0:# and new_length <= min_dst:
                    new_key = graph.nodes[key_pos]['val']
                    keys_collected_new = deepcopy(keys_collected)
                    keys_collected_new.add(new_key)
                    keys_left_new = deepcopy(keys_left)
                    keys_left_new = list(keys_left_new)
                    keys_left_new.remove(key_pos)
                    keys_left_new = tuple(keys_left_new)
                    heappush(q, (new_length, keys_left_new, keys_collected_new, key_pos))

print('RES: ', min_dst)
