from networkx import *
import sys

if (len(sys.argv) != 3):
    print "usage -- provide an input adjlist file and an output adjlist file"

G=read_adjlist(sys.argv[1],delimiter=" ",nodetype=int)

lst = []

i = 0
xlate = {}
for u in G.nodes():
    xlate[u] = i
    i +=1

if (len(G.nodes()) !=100):
    print "wrong lengyh"

for key in xlate.keys():
    if xlate[key] != key:
        print "need to translate"

exit

for u in G.nodes():
    for v in G.neighbors(u):
        G.add_edge(xlate[u],xlate[v])

write_adjlist(G,path=sys.argv[2],delimiter=" ")
