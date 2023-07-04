#Pj 5 Session 7 Problem
#Muhammad Rahmani
import networkx as nx
from itertools import product

G = nx.read_edgelist('soc-sign-epinions.txt', nodetype=int, data=(('weight', float),), create_using=nx.Graph())

P_edges = sum(1 for _, _, sign in G.edges(data='weight') if sign > 0)
N_edges = sum(1 for _, _, sign in G.edges(data='weight') if sign < 0)

total_edges = P_edges + N_edges

P_fraction = P_edges / total_edges
N_fraction = N_edges / total_edges

triad_probabilities = {}

for triad_type in range(16):
    triad_probability = 1.0

    for edge_signs in product([-1, 1], repeat=3):
        sign_product = 1.0

        for sign in edge_signs:
            if sign == 1:
                sign_product *= P_fraction
            else:
                sign_product *= N_fraction

        triad_probability *= sign_product

    triad_probabilities[triad_type] = triad_probability

print(f'Positive Fraction: {P_fraction:.4f}')
print(f'Negative Fraction: {N_fraction:.4f}')
print('Triad Probabilities:')
for triad_type, probability in triad_probabilities.items():
    print(f'Triad {triad_type}: Probability = {probability:.4f}')
print("Muhammad Rahmani")