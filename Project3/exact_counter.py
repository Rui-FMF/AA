# Rui Fernandes
# Nmec: 92952

import sys

def main():
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]
    
    word_list = []

    with open('./files/'+file_name, 'r', encoding='utf-8') as read_file:   
        for line in read_file:
            for word in line.split():
                if word not in word_list:
                    word_list.append(word)
    
    print('Number of unique words in text: '+str(len(word_list)))
    
    with open('./results/'+file_name[:-4]+'_exact_count.txt', 'w', encoding='utf-8') as results_file:
        results_file.write('Number of unique words in text: '+str(len(word_list)))


if __name__== "__main__":
    main()
