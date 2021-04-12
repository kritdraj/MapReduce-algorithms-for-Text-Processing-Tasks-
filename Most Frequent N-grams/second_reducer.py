#!/usr/bin/env python
import sys
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
for i in d:
	print(i,d[i])
