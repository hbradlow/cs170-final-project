import os 
from web.apps.solver import solver 
def run():
	l = os.listdir("inputs")
	for i in l:
		if i.find("translated")!=-1 and i.find("adjlist")!=-1 and i.find("out")==-1: 
			print "File: ",i
			try:
				solver.run("inputs/" + i)
			except:
				print "THat one failed.."

if __name__=="__main__":
	run()
