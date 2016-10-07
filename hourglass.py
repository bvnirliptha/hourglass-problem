#!/usr/bin/python -tt


import sys
import numpy as np

list_sum=[]

def main():
	
	inp_array = input()
	array = np.array(inp_array)
	(row,col) = array.shape

	for i in range(row-2):
	  for j in range(col-2):
	    slice = array[[[i],[i+2]],[j,j+1,j+2]]
		hourglass = np.append(slice.array[i+1,j+1)
		sum = np.sum(hourglass)
		list_sum.append(sum)
		
	max_sum=max(list_sum)
	print max_sum





if __name__ == '__main__':
	main()