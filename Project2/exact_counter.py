# Rui Fernandes
# Nmec: 92952
import json
import sys
import string

def main():
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]

    valid_letters = string.ascii_uppercase
    
    counter_dict = dict()

    with open('./files/'+file_name, 'r', encoding='utf-8') as read_file:
        while True:
            c = read_file.read(1)
            if not c:
                break
            
            if c in valid_letters:
                if c in counter_dict:
                    counter_dict[c]+=1
                else:
                    counter_dict[c]=1
    
    counter_dict = {'total_count':sum(counter_dict.values()), 'chars': dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True))}
    print(counter_dict)

    with open('./results/'+file_name[:-4]+'_exact_results.txt', 'w', encoding='utf-8') as results_file:
            results_file.write(json.dumps(counter_dict, ensure_ascii=False))


if __name__== "__main__":
    main()
