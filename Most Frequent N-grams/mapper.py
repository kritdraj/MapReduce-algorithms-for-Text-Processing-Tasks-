#!/usr/bin/env python3

import sys
import re
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

def read_input(file):
	for i in file:
		for j in i.split():
			yield j

lem= WordNetLemmatizer()

def main():
	k=read_input(sys.stdin)
	#print(k)
	a=[]
	for words in k:
		words = words.lower()
		c= re.findall('[a-zA-Z]+', words)
		#print(c)
		
		a.extend(c) #list
	#print(a) 
	#print(len(a))
	A = []
	for i in range(len(a)):
		mod = lem.lemmatize(a[i], 'n')
		A.append(mod)

	kw= ['science','sea','fire']
	i = 0
	for i in range(len(A)):
		if A[i] in kw:
			#print(a[i])
			seq1 = ' '.join(A[i-2:i+1])
			seq2 = ' '.join(A[i-1:i+2])
			seq3 = ' '.join(A[i:i+3])
			#print(seq1)
			#print(seq2)
			#print(seq3)

			x = re.sub(A[i], '$', seq1)
			y = re.sub(A[i], '$', seq2)
			z = re.sub(A[i], '$', seq3)

			print(re.sub(' ', '_', x), 1)
			print(re.sub(' ', '_', y), 1)
			print(re.sub(' ', '_', z), 1)
			print("\n")
		
		

	
				
	
	
	


if __name__ =="__main__":
	main()



