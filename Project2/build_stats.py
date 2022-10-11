# Rui Fernandes
# Nmec: 92952
import json
import sys
import random
import string
import numpy

def main():
    args = sys.argv[1:]

    if len(args)<3:
        raise Exception("Too little arguments")

    original_file_name = args[0]
    results_file_name = args[1]
    method = args[2]

    
    with open('./results/'+original_file_name[:-4]+'_exact_results.txt', 'r') as real:
        real_vals = json.loads(real.read())

    real_total = real_vals['total_count']
    real_order = "".join(real_vals['chars'].keys())
    real_order_top5 = real_order[:5]

    total_list = []
    order_dict = dict()
    top5_order_dict = dict()

    letter_counts = dict.fromkeys(string.ascii_uppercase,0)


    with open('./results/'+results_file_name, 'r', encoding='utf-8') as read_file:
        while True:
            d = read_file.readline()
            if not d:
                break
            d = json.loads(d)

            total = sum(d.values())
            total_list.append(total)

            for c in list(d.items()):
                letter_counts[c[0]]+=c[1]

            order = "".join(d.keys())
            if order in order_dict:
                order_dict[order]+=1
            else:
                order_dict[order]=1

            if order[:5] in top5_order_dict:
                top5_order_dict[order[:5]]+=1
            else:
                top5_order_dict[order[:5]]=1

    order_dict = dict(sorted(order_dict.items(), key=lambda item: item[1], reverse=True))
    top5_order_dict = dict(sorted(top5_order_dict.items(), key=lambda item: item[1], reverse=True))

    if method=='F':
        EV = real_total/64
        EV_dict = {key:value/64 for (key,value) in real_vals['chars'].items()}
        V = real_total/128
        SD = numpy.sqrt(real_total)/64
    else:
        EV = numpy.log2( real_total*(numpy.sqrt(2)-1) + numpy.sqrt(2)-1 )/2
        EV_dict = {key:numpy.log2( value*(numpy.sqrt(2)-1) + numpy.sqrt(2)-1 )/2 for (key,value) in real_vals['chars'].items()}
        V = EV/2
        SD = numpy.sqrt(V)


    n = len(total_list)
    mean = sum(total_list)/n
    MAE = sum([abs(x - mean) for x in total_list])/n

    MAD = sum([(x - mean) for x in total_list])/n
    variance = sum([(x - mean) ** 2 for x in total_list])/n

    MAX = max(total_list)
    MIN = min(total_list)

    MD = abs(MAX-mean) if abs(MAX-mean)>abs(MIN-mean) else abs(MIN-mean)
    
    letter_counts = dict(sorted({key:value/n for (key,value) in letter_counts.items()}.items(), key=lambda item: item[1], reverse=True))

    with open('./results/'+original_file_name[:-4]+'_'+method+'_stats.txt', 'w') as stats:
        stats.write(f'Expected Value: {round(EV,3)}\n')
        stats.write(f'Variance: {round(V,3)}\n')
        stats.write(f'Standard Deviation: {round(SD,3)}\n\n')

        stats.write(f'Mean Absolute Error: {round(MAE,3)}\n')
        stats.write(f'Mean Relative Error: {round(MAE/EV*100,3)}%\n')
        stats.write(f'Mean Accuracy Ratio: {round(mean/EV*100,3)}%\n\n')

        stats.write(f'Smallest Counter Value: {MIN}\n')
        stats.write(f'Largest Counter Value: {MAX}\n\n')
        
        stats.write(f'Mean Counter Value: {round(mean,3)}\n')
        stats.write(f'Mean Absolute Deviation: {MAD}\n')
        stats.write(f'Standard Deviation: {round(numpy.sqrt(variance),3)}\n')
        stats.write(f'Maximum Deviation: {round(MD,3)}\n')
        stats.write(f'Variance: {round(variance,3)}\n\n\n')
        

        stats.write(f'Real Char Frequency Order: {real_order}\n')
        stats.write(f'Char Order Accuracy: {round(order_dict[real_order]/n*100,3) if real_order in order_dict else 0}%\n')
        stats.write('10 Most Common Orders:\n')
        for o in list(order_dict.items())[:10]:
            stats.write(f'{o[0]} : {o[1]}\n')
        
        stats.write('\n')
        stats.write(f'Top 5 Char Order Accuracy: {round(top5_order_dict[real_order_top5]/n*100,3) if real_order_top5 in top5_order_dict else 0}%\n')
        stats.write('10 Most Common Orders:\n')
        for o in list(top5_order_dict.items())[:10]:
            stats.write(f'{o[0]} : {o[1]}\n')

        stats.write('\n\n\n')
        stats.write('Mean Counter Values per letter:\n')
        stats.write(f'Letter : Counter Value : Expected Value\n')
        for l in list(letter_counts.items()):
            stats.write(f'{l[0]} : {l[1]} : {EV_dict[l[0]]}\n')

if __name__== "__main__":
    main()
