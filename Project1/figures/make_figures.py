import math

import pandas as pd
import matplotlib.pyplot as plt
def no_iterations(brute_force, greedy):
    x = greedy['n']
    y = greedy['iterations']
    plt.scatter(x, y, label="greedy", color="blue",
                s=30)

    # x-axis label
    plt.xlabel('Graph Vertice Number (n)')
    plt.ylabel('Iterations')
    plt.title('Number of Iterations for Greedy')
    # showing legend
    plt.legend()
    plt.savefig('figures/no_iterations_bf.png')
    plt.show()

    # function to show the plot

    x = brute_force['n']
    y = brute_force['iterations']
    plt.scatter(x, y, label="brute force", color="red",
                s=30)

    plt.xlabel('Graph Vertice Number (n)')
    plt.ylabel('Iterations')
    plt.title('Number of Iterations for Brute Force')
    # showing legend
    plt.legend()

    # function to show the plot

    plt.savefig('figures/no_iterations_gr.png')
    plt.show()

    x = greedy['n']
    y = greedy['iterations']
    plt.scatter(x, y, label="greedy", color="blue",
                s=30)


    x = brute_force['n']
    y = brute_force['iterations']
    plt.scatter(x, y, label="brute force", color="red",
                s=30)

    # x-axis label
    plt.xlabel('Graph Vertice Number (n)')
    plt.ylabel('Iterations')
    plt.title('Number of Iterations Comparison')
    # showing legend
    plt.legend()
    plt.savefig('figures/no_iterations_bfgr.png')
    plt.show()

def no_vert_closure(brute_force, greedy):
    x = brute_force['n']
    y = greedy['no_vertices']
    plt.scatter(x, y, label="greedy", color="blue",
                s=30)

    # x-axis label
    plt.xlabel('Graph Vertice Number (n)')
    plt.ylabel('Size of Closure')
    plt.title('Maximum Weighted Closure Size')
    # showing legend
    plt.legend()
    plt.savefig('figures/no_vert_closure_bf.png')
    plt.show()

    # function to show the plot

    x = brute_force['n']
    y = brute_force['no_vertices']
    plt.scatter(x, y, label="brute force", color="red",
                s=30)

    # x-axis label
    plt.xlabel('Graph Vertice Number (n)')
    plt.ylabel('Size of Closure')
    plt.title('Maximum Weighted Closure Size')
    # showing legend
    plt.legend()

    # function to show the plot
    plt.savefig('figures/no_vert_closure_gr.png')
    plt.show()

    x = brute_force['n']
    y = greedy['no_vertices']
    plt.scatter(x, y, label="greedy", color="blue",
                s=30)


    y = brute_force['no_vertices']
    plt.scatter(x, y, label="brute force", color="red",
                s=30)

    # x-axis label
    plt.xlabel('Graph Vertice Number (n)')
    plt.ylabel('Size of Closure')
    plt.title('Maximum Weighted Closure Size')
    # showing legend
    plt.legend()
    plt.savefig('figures/no_vert_closure_bfgr.png')
    plt.show()

def time_per_n(brute_force, greedy):

    x = greedy['n']
    y = greedy['time']
    plt.scatter(x, y, label="greedy", color="blue",
                s=30)

    # x-axis label
    plt.xlabel('Number of Vertices (n)')
    plt.ylabel('Time (s)')
    plt.title('Time to Find a Solution with Greedy')
    # showing legend
    plt.legend()
    plt.savefig('figures/time_per_n_bf.png')
    plt.show()

    # function to show the plot

    x = brute_force['n']
    y = brute_force['time']
    plt.scatter(x, y, label="brute force", color="red",
                s=30)

    # x-axis label
    plt.xlabel('Number of Vertices (n)')
    plt.ylabel('Time (s)')
    plt.title('Time to Find A Solution with Brute Force')
    # showing legend
    plt.legend()

    # function to show the plot
    plt.savefig('figures/time_per_n_gr.png')
    plt.show()

    x = greedy['n']
    y = greedy['time']
    plt.scatter(x, y, label="greedy", color="blue",
                s=30)


    x = brute_force['n']
    y = brute_force['time']
    plt.scatter(x, y, label="brute force", color="red",
                s=30)

    # x-axis label
    plt.xlabel('Number of Vertices (n)')
    # frequency label
    plt.ylabel('Time(s)')
    # plot title
    plt.title('Time to Find A Solution Comparison')
    # showing legend
    plt.legend()
    plt.savefig('figures/time_per_n_bfgr.png')
    plt.show()
def weight_per_n(brute_force, greedy):
    x = greedy['n']
    y = greedy['max_weight']
    plt.scatter(x, y, label="greedy", color="blue",
                s=30)

    # x-axis label
    plt.xlabel('Number of Vertices (n)')
    # frequency label
    plt.ylabel('Total Weight of Max Weight Independent Set')
    # plot title
    plt.title('Maximum Weight Found for Greedy')
    # showing legend
    plt.legend()
    plt.savefig('figures/weight_per_n_bf.png')
    plt.show()

    # function to show the plot

    x = brute_force['n']
    y = brute_force['max_weight']
    plt.scatter(x, y, label="brute force", color="red",
                s=30)

    # x-axis label
    plt.xlabel('Number of Vertices (n)')
    # frequency label
    plt.ylabel('Total Weight of Max Weight Independent Set')
    # plot title
    plt.title('Maximum Weight Found for Brute Force')
    # showing legend
    plt.legend()

    # function to show the plot
    plt.savefig('figures/weight_per_n_gr.png')
    plt.show()

    x = greedy['n']
    y = greedy['max_weight']
    plt.scatter(x, y, label="greedy", color="blue",
                s=30)

    # x-axis label


    # function to show the plot

    x = brute_force['n']
    y = brute_force['max_weight']
    plt.scatter(x, y, label="brute force", color="red",
                s=30)

    # x-axis label
    plt.xlabel('Number of Vertices (n)')
    # frequency label
    plt.ylabel('Total Weight of Max Weight Independent Set')
    # plot title
    plt.title('Maximum Weight Found Comparison')
    # showing legend
    plt.legend()
    plt.savefig('figures/weight_per_n_bfgr.png')
    plt.show()

def calculate_coef(brute_force, greedy):
    y = [y for y in greedy['time']]
    x = [x for x in greedy['iterations']]
    ns = [n for n in greedy['n']]
    relation = [y[i] / (greedy['n'][i] * math.log2(greedy['n'][i])) for i in range(len(x))]
    coeficient = [relation[i] / x[i] for i in range(len(x))]
    coef = sum(coeficient) / len(coeficient)
    plt.scatter(x, relation, label="correlation ~ " + str(coef), color="blue",
                s=30)

    plt.ylabel('Time (s)')
    # frequency label
    plt.xlabel('Iterations')
    # plot title
    plt.title('Time per number of iterations')
    # showing legend
    plt.legend()
    plt.savefig('figures/coef_gr.png')
    plt.show()

    y = [y for y in brute_force['time']]
    x = [x for x in brute_force['iterations']]
    relation = [y[i] / (brute_force['n'][i] ** 2) for i in range(len(x))]
    coeficient = [relation[i] / x[i] for i in range(len(x))]
    coef = sum(coeficient) / len(coeficient)

    plt.scatter(x, relation, label="correlation ~ " + str(coef), color="red",
                s=30)

    plt.ylabel('Time (s)')
    # frequency label
    plt.xlabel('Iterations')
    # plot title
    plt.title('Time per number of iterations')
    # showing legend
    plt.legend()
    plt.savefig('figures/coef_brt.png')
    plt.show()
    # x-axis label

if __name__ == "__main__":
    greedy = pd.read_csv('greedy_results.csv')
    brute_force = pd.read_csv('brute_force_results.csv')
    #weight_per_n(brute_force, greedy)
    #time_per_n(brute_force,greedy)
    #no_vert_closure(brute_force,greedy)
    #no_iterations(brute_force,greedy)
    calculate_coef(brute_force,greedy)
