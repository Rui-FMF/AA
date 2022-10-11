# Rui Fernandes
# Nmec: 92952
from cProfile import label
import json
import sys
import matplotlib.pyplot as plt

def build_graph(f,name):
    for k in f.keys():
        plt.plot(f[k]["sizes"], f[k]["counts"], marker='o', label=str(k)+" functions")
    
    plt.plot(f[k]["sizes"], [13564 for i in range(0,20)], label="exact count")
    
    plt.title("Counts for hash function of "+name)
    plt.xlabel("Size of Bloom Filter")
    plt.ylabel("Estimated Unique Word Count")
    plt.legend()
    plt.show()

def main():


    data = { "builtins":{}, "mmh3":{}, "fnv":{} }

    with open('./results/Odyssey_bloom_counts.txt', 'r') as result_file:
        for line in result_file:
            d = json.loads(line)
            if d["number_of_hashes"] in data[d["hash_function"]]:
                data[d["hash_function"]][d["number_of_hashes"]]["sizes"].append(d["size"])
                data[d["hash_function"]][d["number_of_hashes"]]["counts"].append(d["estimated_count"])
            else:
                data[d["hash_function"]][d["number_of_hashes"]] = {"sizes":[d["size"]], "counts":[d["estimated_count"]]}

    for f in data.keys():
        build_graph(data[f],f)

if __name__== "__main__":
    main()
