#!/usr/bin/env python3
import sys
import re
import os

for i in sys.stdin:
	for wd in i.strip().split():
		#to get file path
		name=os.getenv('map_input_file')
		#to get just the file name
		s,dname=os.path.split(name)
		a=re.findall('[a-zA-Z]+',wd.lower())
		k="".join(a)
		if(k!=""):
			print(dname,k)
			#file name and word

