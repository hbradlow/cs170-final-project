import sys
sys.path.append("/home/ff/cs170/project-2012/lib/python2.7/site-packages/")
from networkx import *
import sys

if (len(sys.argv) != 2):
    print "usage -- provide an input adjlist file and an output adjlist file"

G=read_adjlist(sys.argv[1],delimiter=" ",nodetype=int)

lst = []

i = 0
xlate = {}
for u in G.nodes():
    xlate[u] = i
    i +=1

if (len(G.nodes()) !=100):
    print "wrong lengyh", sys.argv[1]

for key in xlate.keys():
    if xlate[key] != key:
        print "need to translate ", sys.argv[1]
        break
