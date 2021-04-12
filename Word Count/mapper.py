#!/usr/bin/env python3
import sys
import re
def read_input(file):
  for i in file:
    for j in i.split():
      yield j

def main():
	k=read_input(sys.stdin)
	for f in k:
		for i in f.split():
			j=re.findall('[a-zA-Z]+',i)
			j=" ".join(j)
			j=j.split()
			#j=j.split(".")
			#j=" ".join(j)
			for i in j:
				if (i!=" "):
					print(i.lower(),1)
	
	
	
	


if __name__ =="__main__":
	main()
