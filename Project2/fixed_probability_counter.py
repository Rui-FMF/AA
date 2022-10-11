# Rui Fernandes
# Nmec: 92952
import json
import sys
import random
import string

def main():
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]

    valid_letters = string.ascii_uppercase
    
    counter_dict = dict()
    probability = 1/64
    iterations = 10000

    
    with open('./results/'+file_name[:-4]+'_fixed_prob_results.txt', 'w', encoding='utf-8') as results_file:
        for i in range(0,iterations):
            with open('./files/'+file_name, 'r', encoding='utf-8') as read_file:
                while True:
                    c = read_file.read(1)
                    if not c:
                        break
                    
                    if c in valid_letters and (random.random()<=probability):
                        if c in counter_dict:
                            counter_dict[c]+=1
                        else:
                            counter_dict[c]=1
        
                counter_dict = dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True))

                results_file.write(json.dumps(counter_dict, ensure_ascii=False))
                results_file.write('\n')

                counter_dict = dict()


if __name__== "__main__":
    main()
