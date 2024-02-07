# comparison of various Fifo data structure implementations
# based on a comp.lang.python posting by Tim Delaney
# David Eppstein, UCI, 16 Jan 2002

import time
import string
import array

class DictIntFifo:

	def __init__(self):
		self.data = {}
		self.nextin = 0
		self.nextout = 0

	def append(self, value):

		self.data[self.nextin] = value

		try:
			self.nextin += 1
		except OverflowError:
			self.nextin += long(1)

	def pop(self):
		value = self.data[self.nextout]
		del self.data[self.nextout]

		try:
			self.nextout += 1
		except OverflowError:
			self.nextout += long(1)

		return value

class DictLongFifo:

	def __init__(self):
		self.data = {}
		self.nextin = long(0)
		self.nextout = long(0)

	def append(self, value):

		self.data[self.nextin] = value
		self.nextin += 1

	def pop(self):
		value = self.data[self.nextout]
		del self.data[self.nextout]
		self.nextout += 1
		return value

class ListPrependFifo:
	""""""
	
	def __init__(self):
		""""""
		self.data = []

	def append(self, value):
		self.data.insert(0, value)

	def pop(self):
		return self.data.pop()

class ListAppendFifo:
	""""""
	
	def __init__(self):
		""""""
		self.data = []

	def append(self, value):
		self.data.append(value)

	def pop(self):
		return self.data.pop(0)

class ListIndexFifo:
	""""""
	
	def __init__(self):
		""""""
		self.data = []
		self.index = -1

	def append(self, value):
		self.data.append(value)

	def pop(self):
		self.index = self.index + 1
		if self.index > len(self.data) / 2:
			self.data = self.data[self.index:]
			self.index = 0
		return self.data[self.index]

def test (fifo, iterations):
	""""""

	start = time.clock()

	for i in xrange(iterations):
		fifo.append(i)
	for i in xrange(iterations):
		j = fifo.pop()

	end = time.clock()

	try:
		name = fifo.__class__.__name__
	except:
		name = type(fifo)

	print "%-8s %-20s %-06f" % (iterations, name, end - start,)

for i in xrange(3):
	
	print
	test([], 10**(i + 3))
	test(array.array('i'), 10**(i + 3))
	test(DictIntFifo(), 10**(i + 3))
	test(DictLongFifo(), 10**(i + 3))
	test(ListPrependFifo(), 10**(i + 3))
	test(ListAppendFifo(), 10**(i + 3))
	test(ListIndexFifo(), 10**(i+3))

