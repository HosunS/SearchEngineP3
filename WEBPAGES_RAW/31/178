from goody import irange


class Queue:
    """
    Implements a Queue data type: values are removed
      according to the first-in-first-out (FIFO) rule.
    """
    def __init__(self,inital_contents=[]):
        """
        Queue is constructed to store initial_contents (it can be any iterable).
        """
        print('in _init_')
        self._values  = [i for i in inital_contents]


    def add(self,v):
        """
        Add value v to the queue
        """
        self._values.append(v)
 
        
    def remove(self):
        """
        Remove and return the value at the front of the queue 
        """
        assert not self.is_empty(), 'Queue:remove empty'
        answer = self._values[0]
        self._values = self._values[1:]
        return answer

 
    def clear(self):
        """
        Clear the queue
        """
        self._values = [];
  
        
    def peek(self):
        """
        Return (but do not remove) the value at the front of the queue
        """
        assert not self.is_empty(), 'Queue:peek empty'
        return self._values[0]
 
        
    def is_empty(self):
        """
        Return whether the queue is empty
        """
        return self.size() == 0       


    def size(self):
        """
        Return the number of values in the queue
        """
        return len(self._values)        


    def __str__(self):
        """
        Return a string representation of a queue
        """
        return str(self._values)


    def __iter__(self):
        """
        Implement the constructor for the iterator protocol
        """
        return iter(list(self._values))
 
    
    def __add__(self,x):
        """
        Overload syntax: q = q + x is the same as q.add(x)
        """
        self.add(x)
        return self
        
        
    def __bool__(self):
        """
        Determine the truth of a queue: non-empty queues are True
        """
        return not self.is_empty()

  
  
  
        
if __name__ == '__main__': 
    import prompt
    print('Begin testing Queue') 
    command_prompt = \
"""\nTesting Queue:
Commands     Queries         Other
  a - add      p - peek        . - exec(...)
  r - remove   e - is_empty    i - iterator
  c - clear    s - size        q - quit
               _ - __str__
               
Command""" 
    q = eval('Queue('+input('q = Queue('))
    while True:
        action = prompt.for_char(command_prompt, legal='arcpes_.iq')
        try:
            if   action == 'a': q.add(prompt.for_string('  Enter value to add'))
            elif action == 'r': print('  remove =',q.remove())
            elif action == 'c': q.clear()
            
            elif action == 'p': print('  peek =',q.peek())
            elif action == 'e': print('  is_empty =',q.is_empty())
            elif action == 's': print('  size =',q.size())
            elif action == '_': print('  str =',q)
            
            elif action == '.': exec(prompt.for_string('  Enter command to exec (instance=q)'))
            elif action == 'i': print('  iteration order =',[i for i in q])
            elif action == 'q': break
            else: print('  Unknown command')
        except AssertionError as report:
            print('  AssertionError exception caught:', report)
        except Exception as report:
            import traceback
            traceback.print_exc()
    print('\nFinished testing Queue')