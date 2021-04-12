#!/usr/bin/env python3
import sys
def read_mapper_output(file):
	for i in file:
		for j in i.split():
			yield j

def main():
	g={}
	k=read_mapper_output(sys.stdin)
	for j in k:
			f=j.split()
			for l in f:
				if l.isalpha() and l in g:g[l]+=1
				else:g[l]=1
	for i in g:print(i,g[i])
		
	
	
	


if __name__ =="__main__":
	main()
