import sys
sys.path.append("/home/ff/cs170/project-2012/lib/python2.7/site-packages/")
#print sys.path
from networkx import *

sol_file = sys.argv[1]
#filenames = sys.argv[1:]

f = open(sol_file)
global results

results = [-1 for x in xrange(65)]

#print results

def grabnum(fname):
    val = -1
    try:
        val = int(fname.split('.')[0])
    except:
        val = -1
    return val

def report_result(instanceNum,val):
    results[instanceNum] = val

def check_file(fname, sol):
    G=read_adjlist(path=fname,delimiter=" ",nodetype=int)
    instanceNum = grabnum(fname)
    if (sol == 'disconnected' or sol == 'DISCONNECTED'):
        if (not is_connected(G)):
            report_result(instanceNum,0)
        else:
            report_result(instanceNum,200)
    else:
        nodes = sol
        if  not (len(node_boundary(G,nodes))+len(nodes) 
                 == G.number_of_nodes()):
            print "your solution for ", fname, " is not dominating "
            report_result(instanceNum,200)
        elif not is_connected(G.subgraph(nodes)):
            print "your solution for ", fname, " is not connected "
            report_result(instanceNum,200)
        else:
            report_result(instanceNum, len(nodes))

for line in f:
    fields = line.split()
    fname = fields[0]
    if (fields[1] == 'disconnected'):
        check_file(fname, fields[1])
    else:
        sol = []
        for i in xrange(1,len(fields)):
            sol.append(int(fields[i]))
        check_file(fname, sol)

print results
