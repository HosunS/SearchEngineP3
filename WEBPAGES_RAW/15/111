# Merge sort, compact but inefficient (O(n^2)) implementation
# David Eppstein, UCI, 10 Jan 2002

def mergesort(L):
	if len(L) < 2: return L
	return merge(mergesort(L[:len(L)/2]),mergesort(L[len(L)/2:]))

def merge(A,B):
	Out = []
	while len(A)+len(B) > 0:
		if len(B) == 0 or (len(A) > 0 and A[0] < B[0]):
			Out.append(A[0])
			A = A[1:]
		else:
			Out.append(B[0])
			B = B[1:]
	return Out

print mergesort([3,4,1,5,9,2,6,5,3,5])
