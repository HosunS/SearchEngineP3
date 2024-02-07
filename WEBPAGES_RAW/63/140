# find kth element in a list L
# David Eppstein, UC Irvine, 28 Jan 2001

# You wouldn't actually want to use this algorithm -- I wrote it
# for an exam question asking to analyze it.  Its time turns out to be
# T(n) = 2 T(2n/3) + O(n) = O(n^{log_{3/2} 2} = O(n^{1.71}).

def slowSelect(L, k):
	# avoid infinite recursion, throw exception if k out of range
	if len(L) <= 1: return L[k]

	# recursively find median of first 2/3 of L
	pivot = slowSelect(L[:2*len(L)/3], len(L)/3)
	
	# three-way partition
	A = [x for x in L if x < pivot]
	B = [x for x in L if x == pivot]
	C = [x for x in L if x > pivot]

	# continue in one of the three sublists
	if len(A) > k: return slowSelect(A,k)
	elif len(A) + len(B) <= k: return slowSelect(C, k - len(A) - len(B))
	else: return pivot


# test: should produce array in sorted order
for i in range(14):
	print slowSelect([3,1,4,1,5,9,2,6,5,3,5,8,9,7],i)
