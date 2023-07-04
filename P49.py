#Pj 5 Session 7 Problem
#Muhammad Rahmani
import networkx as nx
import random

def is_balanced(G):
    for node in G.nodes():
        pos_edges = sum(1 for _, _, sign in G.edges(node, data='sign') if sign == 1)
        neg_edges = sum(1 for _, _, sign in G.edges(node, data='sign') if sign == -1)

        if pos_edges != neg_edges:
            return False

    return True

def generate_random_signed_network():
    G = nx.complete_graph(10)

    for _, _, data in G.edges(data=True):
        data['sign'] = random.choice([-1, 1])

    return G

def run_dynamic_process(G, iterations=1000000):
    for _ in range(iterations):
        node = random.choice(list(G.nodes()))
        neighbor1, neighbor2 = random.sample(list(G.neighbors(node)), 2)
        edge1 = G[node][neighbor1]
        edge2 = G[node][neighbor2]

        if edge1['sign'] == edge2['sign']:
            G[node][neighbor1]['sign'] = 1
            G[node][neighbor2]['sign'] = 1
        else:
            G[node][neighbor1]['sign'] = -1
            G[node][neighbor2]['sign'] = -1

num_balanced_networks = 0
num_iterations = 100

for _ in range(num_iterations):
    G = generate_random_signed_network()
    run_dynamic_process(G)

    if is_balanced(G):
        num_balanced_networks += 1

fraction_balanced = num_balanced_networks / num_iterations
print(f'Fraction of balanced networks: {fraction_balanced:.2f}')
