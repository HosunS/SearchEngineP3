from goody import irange


class Stack:
    """
    Implements a Stack data type: values are removed
      according to the Last-in-first-out (LIFO) rule.
    """
    def __init__(self,inital_contents=[]):
        """
        Stack is constructed to store initial_contents (it can be any iterable).
        """
        self._values  = [i for i in inital_contents]


    def add(self,v):
        """
        Add value v to the stack
        """
        self._values.append(v)
 
        
    def remove(self):
        """
        Remove and return the value at the top of the stack 
        """
        assert not self.is_empty(), 'Stack:remove empty'
        return self._values.pop()

 
    def clear(self):
        """
        Clear the stack
        """
        self._values = [];
  
        
    def peek(self):
        """
        Return (but do not remove) the value at the top of the stack
        """
        assert not self.is_empty(), 'Stack:peek empty'
        return self._values[-1]
 
        
    def is_empty(self):
        """
        Return whether the stack is empty
        """
        return self.size() == 0       


    def size(self):
        """
        Return the number of values in the stack
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
        return reversed(self._values)
 
    
    def __add__(self,x):
        """
        Overload syntax: s = s + x is the same as s.add(x)
        """
        self.add(x)
        return self
        
        
    def __bool__(self):
        """
        Determine the truth of a stack: non-empty stacks are True
        """
        return not self.is_empty()

  
  
  
        
if __name__ == '__main__': 
    import prompt
    print('Begin testing Stack') 
    command_prompt = \
"""\nTesting Stack:
Commands     Queries         Other
  a - add      p - peek        . - exec(...)
  r - remove   e - is_empty    i - iterator
  c - clear    s - size        q - quit
               _ - __str__
               
Command""" 
    s = eval('Stack('+input('s = Stack('))
    while True:
        action = prompt.for_char(command_prompt, legal='arcpes_.iq')
        try:
            if   action == 'a': s.add(prompt.for_string('  Enter value to add'))
            elif action == 'r': print('  remove =',s.remove())
            elif action == 'c': s.clear()
            
            elif action == 'p': print('  peek =',s.peek())
            elif action == 'e': print('  is_empty =',s.is_empty())
            elif action == 's': print('  size =',s.size())
            elif action == '_': print('  str =',s)
            
            elif action == '.': exec(prompt.for_string('  Enter command to exec (instance=s)'))
            elif action == 'i': print('  iteration order =',[i for i in s])
            elif action == 'q': break
            else: print('  Unknown command')
        except AssertionError as report:
            print('  AssertionError exception caught:', report)
        except Exception as report:
            import traceback
            traceback.print_exc()
    print('\nFinished testing Stack')