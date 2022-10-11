# Rui Fernandes
# Nmec: 92952

import sys
from bloom_filter import BloomFilter
import mmh3

def bloom_counter(file_name, m, k, hash_fun):
    
    bf = BloomFilter(m, k, hash_fun)

    estimated_count = 0

    with open('./files/'+file_name, 'r', encoding='utf-8') as read_file:   
        for line in read_file:
            for word in line.split():
                if not bf.check(word):
                    bf.insert(word)
                    estimated_count+=1

    print('Estimated count for bloom filter of size '+str(m)+', '+str(k)+' hash functions, using '+str(hash_fun.__module__)+' function, is: '+str(estimated_count))

    return estimated_count

def main():
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]

    estimated_count = bloom_counter(file_name, 20000, 5, mmh3.hash)




if __name__== "__main__":
    main()
