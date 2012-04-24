from networkx import *
import random

G = Graph() 
G.add_nodes_from(range(100))
G.add_edges_from([(random.choice(range(100)),random.choice(range(100))) for i in range(300)])
write_adjlist(G,"graphs/1.adjlist")
