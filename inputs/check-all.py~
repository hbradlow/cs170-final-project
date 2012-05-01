import sys
sys.path.append("/home/ff/cs170/project-2012/lib/python2.7/site-packages/")
from networkx import *

if (len(sys.argv) != 3):
    print "usage -- provide an input adjlist file and an output adjlist file"

print "working on ", sys.argv[1]
G=read_adjlist(sys.argv[1],delimiter=" ",nodetype=int)

Gnew = Graph()

lst = []

i = 0
xlate = {}
for u in G.nodes():
    xlate[u] = i
    i +=1

for u in G.nodes():
    for v in G.neighbors(u):
        Gnew.add_edge(xlate[u],xlate[v])

write_adjlist(Gnew,path=sys.argv[2],delimiter=" ")
