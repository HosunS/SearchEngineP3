# Mergesort using Python 2.2 "simple generators"
# David Eppstein, UCI, 14 Jan 2002
#
# The use of generators ("yield" keyword) causes all the merges to run
# in parallel, producing items only as needed.  Each time we output an item,
# O(log n) of the parallel merges advance a step.  So, this has a similar
# property to heapsort: it can be stopped early, with running time
# O(n + k log n) to produce the first k items.  Someone on comp.lang.python
# measured this as being 800 times slower than Python's internal sort
# routine, though, and the improvement is only a log factor, so it would
# take ridiculously large n for the asymptotic improvement to kick in.

from __future__ import generators

def merge(A,B):
	try:
		Afirst=A.next()
		Aempty=0
	except StopIteration:
		Aempty=1
	try:
		Bfirst=B.next()
		Bempty=0
	except StopIteration:
		Bempty=1
	while not Aempty and not Bempty:
		if Afirst < Bfirst:
			yield Afirst
			try:
				Afirst=A.next()
				Aempty=0
			except StopIteration:
				Aempty=1
		else:
			yield Bfirst
			try:
				Bfirst=B.next()
				Bempty=0
			except StopIteration:
				Bempty=1
        if not Aempty:
                yield Afirst
                while 1:
                        yield A.next()
        if not Bempty:
                yield Bfirst
                while 1:
                        yield B.next()

def mergesort(L):
	if len(L) < 2:
		return iter(L)
	else:
		return merge(mergesort(L[:len(L)/2]),
			     mergesort(L[len(L)/2:]))

print list(mergesort([3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]))
