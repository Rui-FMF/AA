# Rui Fernandes
# Nmec: 92952
import random
import string
from collections import defaultdict
import json

random.seed(92952)

naming = list(string.ascii_letters)

def gen_graph(n):
    
    Vertices = []

    coords = []

    for i in range(0, n):
        while True:
            x = random.randrange(10)
            y = random.randrange(10)
            if (x,y) not in coords:
                coords.append((x,y))
                break
        Vertices.append(( naming[i], (x,y), random.randrange(1,101) ))
    
    Edges = []

    num_of_edges = random.randrange(1, (n*((n-1)/2))+1)

    for i in range(0,num_of_edges):
        while True:
            e1 = random.choice(Vertices)[0]
            e2 = random.choice(Vertices)[0]
            if e1!=e2 and (e1,e2) not in Edges and (e2,e1) not in Edges:
                Edges.append((e1,e2))
                break
    
    return (Vertices,Edges)


for n in range(2, 53):
    V,E = gen_graph(n)

    #Convert Vertice and Edge lists to storable dictionaries
    vertice_dic = {}

    for vertice in V:
        name, data = vertice[0], (vertice[1], vertice[2])
        vertice_dic[name] = data

    adjancency_list = defaultdict(list)
     
    for edge in E:
        a, b = edge[0], edge[1]
        adjancency_list[a].append(b)
        adjancency_list[b].append(a)

    with open('graph'+str(n)+'.txt', 'w') as f:
        f.write(json.dumps(vertice_dic))
        f.write('\n')
        f.write(json.dumps(dict(adjancency_list)))



