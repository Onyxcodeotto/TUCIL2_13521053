# Python program for implementation of Quicksort Sort

import numpy as np
S2 = np.array([[1,3,0,1],[12,30,0,1],[40,50,0,1],[5,1,0,0],[12,10,0,0],[3,4,0,1]])

def partition(S, low, high, axes):

	# choose the rightmost element as pivot
	pivot = S[high][axes]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if S[j][axes] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1
            
			# Swapping element at i with element at j
			swap(S, i, j)

	# Swap the pivot element with the greater element specified by i
	swap(S, i+1, high)

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort


def quickSort(S, low, high, axes):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(S, low, high, axes)

		# Recursive call on the left of pivot
		quickSort(S, low, pi - 1, axes)

		# Recursive call on the right of pivot
		quickSort(S, pi + 1, high, axes)

def swap(S, i, j):
    S[[i, j]] = S[[j, i]]

def sortList(S):
    return (quickSort(S, 0, len(S) - 1, 0))
    
def sortListY(S):
	return (quickSort(S, 0, len(S) - 1, 1))
    
# print(S2)

# sortList(S2)
# # swap(S2, 0, 1)
# # (S2[axes], S2[1]) = (S2[1], S2[0])
# print(len(S2))
# print('Sorted Array in Ascending Order:')
# print(S2)
