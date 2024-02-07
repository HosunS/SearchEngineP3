class EquivalenceClass:
    """
    Implements an Equivalnce class data type: values are added as
      singletons, equivalance classes are merged,  we can ask
      whether two values are in the same equivalance class, and
      we can get a set of equivalence classes (each a set).
    """
    def __init__(self,inital_contents):
        """
        Equivalence class is constructed to store initial_contents
         (it can be any iterable), each a a singleton
        """
        self._parent    = dict()
        self._root_size = dict()
        for i in inital_contents:
            self.add_singleton(i)


    def add_singleton(self,v):
        """
        Add value v as its own singleton
        """
        assert not v in self._parent, 'EquivalenceClass:add_singleton value v('+str(v)+') already exists'
        self._parent[v] = v
        self._root_size[v] = 1
 
        
    def _compress_to_root(self,v):
        """
        return root of tree storing v, making the parent of v and all its ancestors the root 
        """
        assert v in self._parent, 'EquivalenceClass:_compress_to_root value v('+str(v)+') not in equivalence class'
        # find root
        ancestor = v
        while True:
            root = self._parent[ancestor]
            if root is ancestor:
                break
            ancestor = root
        # make this root the parent of v and all its ancestors
        while True:
            if v is root:
                break
            self._parent[v] = root
            v = self._parent[v]
            break
        # return root
        return root

 
    def clear(self):
        """
        Clear the equivalence class
        """
        self._parent = dict();
        self._root_size = dict()

  
        
    def in_same_class(self,a,b):
        """
        return whether a and b are in the same equivalence class, possibly
          shortening some paths to the root 
        """
        return self._compress_to_root(a) == self._compress_to_root(b)
  
        
    def merge_classes_containing(self,a,b):
        """
        Merge the equivalence classes storing a and b, , possibly
          shortening some paths to the root 
        """
        a = self._compress_to_root(a)
        b = self._compress_to_root(b)
        if a == b:
            return
        
        a_size = self._root_size[a]
        b_size = self._root_size[b]
        if a_size > b_size:
            a,b = b,a
        self._parent[a] = b
        self._root_size[b] = a_size+b_size
        del self._root_size[a]
 
        
    def is_singleton(self):
        """
        Return whether there is just one class in the equivalence class
        """
        return self.size() == 1
      


    def size(self):
        """
        Return the number of different (unequivalent) classes
        """
        return len(self._root_size)
      

    def all_classes(self):
        eqv = dict()
        for i in list(self._parent):
            root = self._compress_to_root(i)
            if root in eqv:
                eqv[root].add(i)
            else:
                eqv[root] = set([i])
        
        return tuple([tuple(i) for i in eqv.values()])
            
            
    def __str__(self):
        return '{' + ','.join(['{'+','.join([repr(j) for j in i])+'}' for i in self.all_classes()]) + '}'


    def __iter__(self):
        """
        Implement the constructor for the iterator protocol
        """
        return iter(self.all_classes())

    
    def __add__(self,x):
        """
        Overload syntax: e = e + x is the same as e.add_singleton(x)
        """
        self.add_singleton(x)
        return self
        
        
    def __bool__(self):
        """
        Determine the truth of an equivalence class: non-unitary equivalence classes are True
        """
        return not self.is_singleton()

  
  
  
        
if __name__ == "__main__": 
    import prompt
    print('Begin testing PriorityQueue') 
    command_prompt = \
"""\nTesting PriorityQueue:
Commands        Queries             Other
  a - add...      ? - in_same         . - exec(...)
  m - merge...    e - is_singleton    i - iterator
  c - clear       s - size            q - quit
                  * - all_classes__
                  _ - __str__
               
Command""" 
    e = eval('EquivalenceClass('+input('e = EquivalenceClass('))
    while True:
        action = prompt.for_char(command_prompt, legal='amc?es*_.iq')
        try:
            if   action == 'a': e.add_singleton(prompt.for_string('  Enter value to add as singleton'))
            elif action == 'm':
                a = prompt.for_string('  Enter first  value for merge')
                b = prompt.for_string('  Enter second value for merge')
                e.merge_classes_containing(a,b)
            elif action == 'c': e.clear()
            
            elif action == '?': print('  in_same_classe =',e.in_same_class())
            elif action == 'e': print('  is_singleton =',e.is_singleton())
            elif action == 's': print('  size =',e.size())
            elif action == '_': print('  str =',e)
            elif action == '*': print('  all_classes =',e.all_classes())
            
            elif action == '.': exec(prompt.for_string('  Enter command to exec (instance=e)'))
            elif action == 'i': print('  iteration order =',[i for i in e])
            elif action == 'q': break
            else: print('  Unknown command')
        except AssertionError as report:
            print('  AssertionError exception caught:', report)
        except Exception as report:
            import traceback
            traceback.print_exc()
    print('\nFinished testing PriorityQueue')