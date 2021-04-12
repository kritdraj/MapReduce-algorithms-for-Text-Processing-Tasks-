#!/usr/bin/env python3
import sys

flag=0
name=""
p={}
select=0
for i in sys.stdin:
	for h in i.split():
		for k in h.split():
			#if select%2==0, means the k 				#value we got is a filename, 				#increment the select at end
			if (select%2)==0:
				name=k
			
			#if (select%2)==1 means its a 				#word and checking if k is in 				#dict p else assign filename as 			#value
			if (select%2)==1 and k in p:
				p[k].append(name)
						
			elif (select%2)==1 and k not in p:
				p[k]=[name]
				
		select+=1
for i in p:
	#using set to remove repeated filenames
	unique_doc_id=set(p[i])
	print(i,list(unique_doc_id))

