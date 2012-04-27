from networkx import *
import random

def three_level_graph(path="graphs/10.adjlist"):
	G = Graph()
	size = 5 
	G.add_nodes_from(range(size))

	for i in range(5*size):
		G.add_edges_from([(random.choice(range(size)),random.choice(range(size)))])
	write_adjlist(G,path)

three_level_graph()
