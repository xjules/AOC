from heapq import heappop, heappush
from itertools import chain, count

import networkx as nx

ls = None
with open('input.txt') as f:
    ls = [x[:-1] for x in f.readlines()]

def get_portal(ls, x, y):
    for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        if ls[x+dx][y+dy].isupper():
            return  ''.join(sorted((ls[x+dx][y+dy],ls[x+2*dx][y+2*dy])))
    return None


def make_graph(ls):
    portals = {}
    portals_2 = {}
    # G = nx.grid_2d_graph(len(ls), len(ls[0]), create_using=nx.Graph)
    print(len(ls), len(ls[0]))
    player = None
    goal = None
    G = nx.Graph()
    for x in range(len(ls)):
        for y in range(len(ls[0])):
            # print(ls[x][y],end='')
            if ls[x][y] in ['#',' '] or ls[x][y].isupper():
                # G.remove_node((x, y))
                pass
            elif ls[x][y] == '.':

                if ls[x-1][y] == '.':
                    G.add_edge((x, y), (x-1, y))
                if ls[x][y-1] == '.':
                    G.add_edge((x, y), (x, y-1))

                portal = get_portal(ls, x, y)
                if portal is not None:
                    if portal == 'AA':
                        print('START: ', (x, y))
                        player = (x, y)
                    elif portal == 'ZZ':
                        print('GOAL: ', (x, y))
                        goal = (x, y)
                    if portal in portals:
                        G.add_edge((x, y), portals[portal])
                        print('Connecting {} from {} to {}'.format(portal, (x, y), portals[portal]))
                        portals_2[portal] = (x, y)
                    else:
                        portals[portal] = (x, y)

        # print('')
    print(portals)
    return G, player, goal

graph, player, goal = make_graph(ls)
path = nx.shortest_path(graph, source=player, target=goal)
# path = nx.shortest_path_length(graph, source=player, target=goal)
print(path)
print('RES: ', len(path)-1)