from django import template
from django.utils.safestring import mark_safe
import json
register = template.Library()

@register.filter
def graph(g=None):
	from solver.solver import *
	g = G
	r = {"nodes":[],"links":[]}
	i = 0
	r["num_blacks"] = num_blacks
	for n in g.adjacency_list():
		r['nodes'].append({"nodeName":str(i),"group":"1","color":nodes.values()[i].color})
		for l in n:
			r['links'].append({"source":i,"target":l,"value":1})
		i+=1
	return mark_safe(json.dumps(r))
