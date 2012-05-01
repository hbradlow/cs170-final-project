import sys
sys.path.append("/home/ff/cs170/project-2012/lib/python2.7/site-packages/")
from networkx import *

filenames = sys.argv[1:]

for fn in filenames:
    #print "working on ", fn
    G=read_adjlist(fn,delimiter=" ",nodetype=int)

    if (not is_connected(G)):
        print fn, " is not connected "
        print  connected_components(G)
    elif (len(G.nodes()) != 100):
        print fn, " has ", len(G.nodes()), " nodes. "

