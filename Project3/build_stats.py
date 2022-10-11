# Rui Fernandes
# Nmec: 92952
import json
import sys
from bloom_counter import bloom_counter
import mmh3
import fnv

def main():

    file_name = 'Odyssey.txt'

    # Exact count of unique words obtained with exact_counter.py
    exact_count = 13564

    results_list = []

    for hash_f in [hash, mmh3.hash, fnv.hash]:
        for k in range(5,11):
            for m in [int(exact_count*(i+j)) for i in range(1,11) for j in [0,0.5]]:
                estimated_count = bloom_counter(file_name, m, k, hash_f)
                results_dict = dict()
                results_dict['size']=m
                results_dict['number_of_hashes']=k
                results_dict['hash_function']=str(hash_f.__module__)
                results_dict['estimated_count']=estimated_count
                results_list.append(results_dict)



    with open('./results/'+file_name[:-4]+'_bloom_counts.txt', 'w') as stats:
        for d in results_list:
            stats.write(json.dumps(d, ensure_ascii=False))
            stats.write('\n')

if __name__== "__main__":
    main()
