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

    for L in range(1, len(Vertices)+1):
        for subset in itertools.combinations(Vertices.keys(), L):
            iterations+=1
            #if not independent then skip
            if check_independance(subset,Edges)==False:
                continue
            weight = sum([Vertices.get(v)[1] for v in subset])
            
            if weight>max_weight: 
                max_weight=weight 
                max_set=subset

    return max_weight, max_set, iterations

with open('brute_force_results.txt', 'w') as result_file:
    result_file.write("n max_weight iterations time\n")

    for n in range(2, 31):
        V,E = read_graph(n)
        
        start_time = time.time()

        W,S,iterations = get_solution(n,V,E)

        exec_time = (time.time() - start_time)

        result_file.write("%s %s %s %s\n" % (n, W, iterations, exec_time))
