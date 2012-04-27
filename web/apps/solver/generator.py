from networkx import *
import random

def three_level_graph(x = 2,path="graphs/1.adjlist"):
	G = Graph()
	G.add_nodes_from(range(7*x))

	for i in range(x):
		G.add_edges_from([(i,a) for a in range(x+i*3,3+i*3+x)])
#		G.add_edges_from([(i,a) for a in range(0,x) if (a>i)])
		if i!=x-1:
			G.add_edges_from([(i,i+1)])
	for i in range(x,4*x):
		G.add_edges_from([(i,i+3*x)])
		if i!=4*x-1:
			G.add_edges_from([(i,i+1)])
	write_adjlist(G,path)

three_level_graph(14)
