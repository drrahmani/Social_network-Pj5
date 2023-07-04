#Pj 5 Session 7 Problem
#Muhammad Rahmani
import networkx as nx

G = nx.read_edgelist('soc-sign-epinions.txt', nodetype=int, data=(('weight', float),), create_using=nx.Graph())

T_counts = nx.triangles(G)

total_triads = sum (T_counts.values())

T_fractions = {triad_type: count / total_triads for triad_type, count in T_counts.items()}

for triad_type, count in T_counts.items():
    fraction = T_fractions[triad_type]
    print(f'Triad {triad_type}: Count = {count}, Fraction = {fraction:.4f}')
print("Muhammad Rahmani")