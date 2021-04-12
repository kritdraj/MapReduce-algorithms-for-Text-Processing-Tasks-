#!/usr/bin/env python3
import sys
from heapq import nlargest

d={}
f=sys.stdin
f=f.read().split("\n")
for i in f:
	if(i!=""):
		i=i.split()
		if i[0] not in d:
			d[i[0]]=int(i[1])
		else:
			d[i[0]]=d[i[0]]+int(i[1])


most_common = nlargest(10, d, key=d.get)

for i in range(len(most_common)):
	print( most_common[i], d[most_common[i]] )