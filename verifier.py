"""
(author: Raf 4/18/2012)
Simple verifyier for the connected dominating set problem.
For more help on NetworkX, start here:
  http://networkx.lanl.gov/tutorial/tutorial.html
"""

import sys
sys.path.append("/home/ff/cs170/project-2012/lib/python2.7/site-packages/")
#print sys.path
from networkx import *


# read example in as an adjacency list
# watch out for trailing whitespace!
G=read_adjlist(path="example.adjlist",delimiter=" ",nodetype=int)

# print out the graph
print 'adjacency list of the input is:'
print G.adjacency_list()
print G

# draw the graph
# import matplotlib.pyplot as plt
# draw_spring(G)
# plt.show()

# read in the solution
f = open('answer1.txt')
nodes = [int(x) for x in f.readline().split()]
print 'suggested connected dominating set:', nodes

# check whether this set of nodes is dominating
if len(node_boundary(G,nodes))+len(nodes) == G.number_of_nodes():
	print "domination: check"
else:
	print "domination: fail! not a connected *dominating* set!"
	print "*** missing nodes:", \
		  list(set(G.nodes()) - (set(node_boundary(G,nodes)+nodes)))

# check to see if these nodes induce a connected subgraph
if is_connected(G.subgraph(nodes)):
	print "connectivity: check"
else:
	print "connectivity: fail! not a *connected* dominating set!"

# write out the example again, just for kicks
write_adjlist(G,path="out.adjlist",delimiter=" ")
