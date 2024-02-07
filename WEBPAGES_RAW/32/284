from goody import irange


class PriorityQueue:
    """
    Implements a Priority Queue data type: values are removed
      according to the highest priority value first rule.
    """
    def __init__(self,inital_contents=[], key=(lambda x: x), reverse=False):
        """
        Priority queue is constructed to store initial_contents (it can be any iterable),
          with key/reverse used for computing relative priorities (as in sorting).
        """
        self._values  = [i for i in inital_contents]
        self._key     = key
        self._reverse = reverse
        self._heapify()


    def _trichotomy(self,x,y):
        x = self._key(x)
        y = self._key(y)
        ans = -1 if x < y else 1 if x > y else 0
        return -ans if self._reverse else ans
    
    
    @staticmethod # avoids syntax error for method below
    def _left_child(i):
        """
        return index of the left child of the value at index i
        """
        return 2*i+1

    @staticmethod # avoids syntax error for method below
    def _right_child(i):
        """
        return index of the right child of the value at index i
        """
        return 2*i+2

   
    @staticmethod # avoids syntax error for method below
    def _parent(i):
        """
        return index of the _parent of the value at index i
        """
        return (i-1)//2

    
    def _heapify(self):
        """
        Linear-time algorithm for converting a list into a heap
        """
        for i in irange(len(self._values)-1,0,-1):
            self._percolate_down(i);

            
    def _in_heap(self,i):
        return 0 <= i < len(self._values)

    
    def _swap(self,i,j):
        """
        Swap the values at indexes i and j
        """
        self._values[i], self._values[j] = self._values[j], self._values[i]
 
        
    def _percolate_up(self,i):
        """
        Percolate up the value at index i, as far as it needs to go in the heap
        """
        while True:
            p = PriorityQueue._parent(i)
            if i <= 0 or self._trichotomy(self._values[p] , self._values[i]) >= 0:
                break
            self._swap(i,p)
            i =  PriorityQueue._parent(i)


    def _percolate_up_recursive(self,i): # not called: could replace percolate_up
        """
        Percolate up the value at index i, as far as it needs to go in the heap
        """
        p =  PriorityQueue._parent(i)
        if i <= 0 or self._trichotomy(self._values[p] , self._values[i]) >= 0:
            return
        self._swap(i,p)
        self._percolate_up2(PriorityQueue._parent(i))


    def _percolate_down(self,i):
        """
        Percolate down the value at index i, as far as it needs to go in the heap
        """
        while True:
            left =  PriorityQueue._left_child(i)
            if not self._in_heap(left):  #No children
                break
            right =  PriorityQueue._right_child(i)
            testChild = left if not self._in_heap(right) or self._trichotomy(self._values[left],self._values[right]) >= 0 else right
            if  self._trichotomy(self._values[i],self._values[testChild]) >= 0:
                break; 
            self._swap(i,testChild)
            i = testChild

                
    def add(self,v):
        """
        Add value v to the priority queue
        """
        self._values.append(v)
        self._percolate_up(len(self._values)-1)
 
        
    def remove(self):
        """
        Remove and return the highest priority value (by key/reverse) in the priority queue 
        """
        assert not self.is_empty(), 'PriorityQueue:remove empty'
        answer          = self._values[0]
        self._values[0] = self._values[-1] 
        self._values.pop()                  #cannot store into empty (after pop) list
        self._percolate_down(0)
        return answer

 
    def clear(self):
        """
        Clear the priority queue
        """
        self._values = [];
  
        
    def merge(self,other):
        """
        Merge other (a PriorityQueue) with this one (clearing otherPriorityQueue)
        """
        self._values += other._values
        self._heapify()
        other.clear()
  
        
    def peek(self):
        """
        Return (but do not remove) the highest priority value in the priority queue
        """
        assert not self.is_empty(), 'PriorityQueue:peek empty'
        return self._values[0]
 
        
    def is_empty(self):
        """
        Return whether the priority queue is empty
        """
        return self.size() == 0       


    def size(self):
        """
        Return the number of values in the priority queue
        """
        return len(self._values)        


    def __str__(self):
        """
        Return a string representation of a priority queue
        """
        return str(self._values)


    def __iter__(self):
        """
        Implement the constructor for the iterator protocol
        """
        copy = PriorityQueue(key=self._key,reverse=self._reverse)
        copy._values = list(self._values)
        return copy#copy._gen()
 
    
    def __next__(self):
        """
        Implement next for the iterator protocol
        """
        if self.is_empty():
            raise StopIteration()
        else:
            return self.remove()
 
        
    def _gen(self):
        while True:
            if self.is_empty():
                raise StopIteration()
            else:
                yield self.remove()
                
    def __add__(self,x):
        """
        Overload syntax: pq = pq + x is the same as pq.add(x)
        """
        self.add(x)
        return self
        
        
    def __bool__(self):
        """
        Determine the truth of a priority queue: non-empty priority queues are True
        """
        return not self.is_empty()

  
  
  
        
if __name__ == '__main__': 
    import prompt
    print('Begin testing PriorityQueue') 
    command_prompt = \
"""\nTesting PriorityQueue:
Commands     Queries         Other
  a - add      p - peek        . - exec(...)
  r - remove   e - is_empty    i - iterator
  c - clear    s - size        q - quit
  m - merge    _ - __str__
               
Command""" 
    pq = eval('PriorityQueue('+input('pq = PriorityeQueue('))
    while True:
        action = prompt.for_char(command_prompt, legal='arcmpes_.iq')
        try:
            if   action == 'a': pq.add(prompt.for_string('  Enter value to add'))
            elif action == 'r': print('  remove =',pq.remove())
            elif action == 'c': pq.clear()
            elif action == 'm': exec('pq.merge('+input('pq.merge('))
            
            elif action == 'p': print('  peek =',pq.peek())
            elif action == 'e': print('  is_empty =',pq.is_empty())
            elif action == 's': print('  size =',pq.size())
            elif action == '_': print('  str =',pq)
            
            elif action == '.': exec(prompt.for_string('  Enter command to exec (instance=pq)'))
            elif action == 'i': print('  iteration order =',[i for i in pq])
            elif action == 'q': break
            else: print('  Unknown command')
        except AssertionError as report:
            print('  AssertionError exception caught:', report)
        except Exception as report:
            import traceback
            traceback.print_exc()
    print('\nFinished testing PriorityQueue')