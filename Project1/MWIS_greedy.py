# Rui Fernandes
# Nmec: 92952
import json
import itertools
import time

def read_graph(n):
    with open('graph'+str(n)+'.txt', 'r') as f:
        v_data = f.readline()
        e_data = f.readline()
    f.close()

    Vertices = json.loads(v_data)
    Edges = json.loads(e_data)

    return Vertices, Edges


def check_independance(subset, Edges):
    for v1 in subset:
        for v2 in subset:
            if v1 in Edges and v2 in Edges.get(v1):
                return False
    return True


def get_solution(n, Vertices, Edges):

    max_weight = 0
    max_set = []
    iterations = 0

    ordered_verticies = sorted( [[vertice[0], vertice[1][1]] for vertice in Vertices.items()] , key=lambda x:x[1])

    while ordered_verticies:
        iterations+=1
        v = ordered_verticies.pop()
        
        max_weight+=v[1]
        max_set.append(v[0])

        ordered_verticies = [v2 for v2 in ordered_verticies if ( v[0] not in Edges or v2[0] not in Edges.get(v[0]) ) ]


    return max_weight, max_set, iterations


with open('greedy_results.txt', 'w') as result_file:
    result_file.write("n max_weight iterations time\n")

    for n in range(2, 53):
        V,E = read_graph(n)
        
        start_time = time.time()

        W,S,iterations = get_solution(n,V,E)

        exec_time = (time.time() - start_time)

        result_file.write("%s %s %s %f\n" % (n, W, iterations, exec_time))