#!/usr/bin/env python3
import sys
from heapq import nlargest



def read_mapper_output(file):
	for i in file:
		for j in i.split():
			yield j

def main():
	g={}
	k=read_mapper_output(sys.stdin)
	for j in k:
			f=j.split()
			#print(f)
			for l in f:
				#print(l)
				if l!='1' and l in g:
					g[l]+=1
				else:g[l]=1
	most_common = nlargest(10, g, key=g.get)
	#print(most_common)
	for i in range(len(most_common)):

		print( most_common[i], g[most_common[i]] )
		

		
	
	
	


if __name__ =="__main__":
	main()
