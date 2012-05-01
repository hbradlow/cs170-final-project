from networkx import *


# read example in as an adjacency list
# watch out for trailing whitespace!
G=read_adjlist(path="graphs/hard.adjlist",delimiter=" ",nodetype=int)

# dictionary with {index:Node}
nodes = {} 
def size_set(nodes):
	s = 0
	for node in nodes.values():
		if node.color=="Black":
			s += 1
	return s
def num_all_black(nodes):
	s = 0
	for node in nodes.values():
		if node.all_black:
			s += 1
	return s


#datastructure to hold nodes
class Node:
	def __init__(self):
		self.color = "White"
		self.number = 0
		self.links = []
		self.all_black = False
	def num_whites(self):
		num = 0
		for l in self.links:
			if nodes[l].color == "White":
				num += 1
		return num
	def num_blacks(self):
		num = 0
		for l in self.links:
			if nodes[l].color == "Black":
				num += 1
		return num
	def __str__(self):
		return self.color + " " + str(self.number)
	def color_map(self):
		if self.color=="White":
			return 0
		if self.color=="Gray":
			return 1
		if self.color=="Black":
			return 2

#method to calculate total number of white nodes
def total_whites():
	num = 0
	for node in nodes.values():
		if node.color=="White":
			num += 1
	return num

#set up nodes from adjaaceny list
i = 0
for node in G.adjacency_list():
	n = Node()
	n.links = node
	n.number = i
	nodes[i] = n
	i += 1

#function to determine node with most white connections
def max_whites(nodes):
	return max(nodes,key = lambda x:x.num_whites()) 

#keep doing process until all nodes are dominated
min_size = 999999 
def start_from(start):
	for node in nodes.values():
		node.color = "White";
		node.all_black = False
	node = start 
	while total_whites()>0:
		node.color = "Black"
		for l in node.links:
			n = nodes[l]
			if n.color != "Black":
				n.color = "Gray"
		node = max_whites([n for n in nodes.values() if n.color=="Gray"]) 

	best = {}
	def post_process():
		i = 0
		for node in nodes.values():
			if node.color=="Black":
				all_black = True
				for l in node.links:
					if nodes[l].color!="Black" and nodes[l].num_blacks()==1:
						all_black = False
				if all_black:
					H = G.subgraph([a for a in range(len(nodes.values())) if a!=i and nodes[a].color=="Black"])
					if is_connected(H):
						node.all_black = True
			i+=1
		for node in nodes.values():
			if num_all_black(nodes)==0:
				if size_set(nodes)<min_size:
					best = nodes.copy()
					global min_size
					min_size = size_set(nodes)
					print min_size 
			if node.all_black:
				node.color = "Gray"
				node.all_black = False
				post_process()
				node.all_black = True 
				node.color = "Black"
					

	post_process()

start = max_whites(nodes.values())
min_list = range(200) 
for start in nodes.values():
	"""
		Try starting the greedy algrorithm for every node, and take the minimium one
	"""
	start_from(start)

	#pull out black nodes
	l = []
	for node in nodes.values():
		if node.color=="Black":
			l.append(node.number)
	num_blacks = len(l)
	if num_blacks<len(min_list):
		min_list = l
	print num_blacks

l = min_list
num_blacks = len(l)
print l
print "Length of list: " + str(len(l))




# check whether this set of nodes is dominating
if len(node_boundary(G,l))+len(l) == G.number_of_nodes():
	print "domination: check"
else:
	print "domination: fail! not a connected *dominating* set!"
	print "*** missing nodes:", \
		  list(set(G.nodes()) - (set(node_boundary(G,l)+l)))
	raise

# check to see if these nodes induce a connected subgraph
if is_connected(G.subgraph(l)):
	print "connectivity: check"
else:
	print "connectivity: fail! not a *connected* dominating set!"
	raise

f = open("my_solution.txt","w")
print " ".join([str(a) for a in l])
f.write(" ".join([str(a) for a in l]))

"""
print "Displaying the graph..." 

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

pos = spring_layout(G,iterations=200)
draw(G,pos,node_color=[node.color_map() for node in nodes.values()], node_size=800,cmap=ListedColormap(['w','.25','.5']))
plt.show()
"""
