class Modular:
    """
    Models a modular number (value and modulus)
    Standard arithmetic operators are overloaded: + - * /
    """
    def __init__(self, value, modulus):
        """
        Instantiate like Modular(3,4)
        """
        assert type(modulus) is int and type(value) is int, \
          'Modular.__init__: Modular('+str(value)+','+str(modulus)+') must both be ints'
        assert modulus >= 1, 'Modular.__init__: modulus('+str(modulus)+') < 1'
        self._value   = value% modulus
        self._modulus = modulus


    def inc(self):
        """
        Increment value (modularly) by 1
        """
        self._value = 0 if self._value == self._modulus-1 else self._value+1 

    
    def dec(self):
        """
        Decrement value (modularly) by 1
        """
        self._value = self._modulus-1 if self._value == 0 else self._value-1 

    
    def clear(self):
        """
        Decrement value (modularly) by 1
        """
        self._value = 0 

    
    def value(self):
        """
        returns current value of modular number
        """
        return self._value 

    
    def modulus(self):
        """
        returns modulus of modular number
        """
        return self._modulus 

    
    def __bool__(self):
        """
        Determine the truth of a Modular value: non-0 values are True
        """
        return self._value != 0


    def __add__(self,other):
        """
        Overload addition operator: +
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__add__: Incompatible modulii'
        if type(other) is Modular:
            return Modular(self._value + other._value, self._modulus)
        else:
            return Modular(self._value + other, self._modulus)


    def __radd__(self,other):
        """
        Overload addition operator (for right operands): +
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__radd__: Incompatible modulii'
        if type(other) is Modular:
            return Modular(other._value + self._value, self._modulus)
        else:
            return Modular(other + self._value, self._modulus)



    def __sub__(self,other):
        """
        Overload subtraction operator: -
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__sub__: Incompatible modulii'
        if type(other) is Modular:
            return Modular(self._value - other._value, self._modulus)
        else:
            return Modular(self._value - other, self._modulus)


    def __rsub__(self,other):
        """
        Overload subtraction operator (for right operands): -
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__rsub__: Incompatible modulii'
        if type(other) is Modular:
            return Modular(other._value - self._value, self._modulus)
        else:
            return Modular(other - self._value, self._modulus)


    def __mul__(self,other):
        """
        Overload multiplication operator: *
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__mul__: Incompatible modulii'
        if type(other) is Modular:
            return Modular(self._value * other._value, self._modulus)
        else:
            return Modular(self._value * other, self._modulus)


    def __rmul__(self,other):
        """
        Overload multiplication operator (for right operands): *
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__rmul__: Incompatible modulii'
        if type(other) is Modular:
            return Modular(other._value * self._value, self._modulus)
        else:
            return Modular(other * self._value, self._modulus)


    def __pow__(self,other):
        """
        Overload power operator: *
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__pow__: Incompatible modulii'
        if type(other) is Modular:
            return Modular(self._value ** other._value, self._modulus)
        else:
            return Modular(self._value ** other, self._modulus)


    def __rpow__(self,other):
        """
        Overload power operator: *
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__rpow__: Incompatible modulii'
        if type(other) is Modular:
            return Modular(other._value ** self._value, self._modulus)
        else:
            return Modular(other ** self._value, self._modulus)


    def __eq__(self,other):
        """
        Overload equal operator: ==
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__eq__: Incompatible modulii'
        if type(other) is Modular:
            return self._value == other._value
        else:
            return self._value == other


    def __ne__(self,other):
        """
        Overload not equal operator: !=
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__ne__: Incompatible modulii'
        if type(other) is Modular:
            return self._value != other._value
        else:
            return self._value != other


    def __lt__(self,other):
        """
        Overload less than operator: <
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__lt__: Incompatible modulii'
        if type(other) is Modular:
            return self._value < other._value
        else:
            return self._value < other


    def __gt__(self,other):
        """
        Overload greater than operator: >
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__gt__: Incompatible modulii'
        if type(other) is Modular:
            return self._value > other._value
        else:
            return self._value > other


    def __le__(self,other):
        """
        Overload less than or equal to operator: <=
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__le__: Incompatible modulii'
        if type(other) is Modular:
            return self._value <= other._value
        else:
            return self._value <= other


    def __ge__(self,other):
        """
        Overload greater than or equal to operator: >
        """
        assert type(other) is not Modular or self._modulus == other._modulus, 'Modular.__ge__: Incompatible modulii'
        if type(other) is Modular:
            return self._value >= other._value
        else:
            return self._value >= other


    def __str__(self):
        """
        Return a string representation for a Modular, such that
        m2 = eval(str(m1)) copies the state of m1 at the time of the call
        """
        return 'Modular('+str(self._value)+','+str(self._modulus)+')'

    



if __name__ == '__main__': 
    import prompt
    print('Begin testing Modular') 
    command_prompt = \
"""\nTesting Modular:
Commands     Queries          Other
  i - inc      v - value        . - exec(...)
  d - dec      m - modulus      q - quit
  c - clear    _  - __str__
  
Command"""                            
    m = Modular(prompt.for_int('Enter value'),prompt.for_int('Enter modulus'))
    while True:
        action = prompt.for_char(command_prompt, legal='idc_.q')
        try:
            if   action == 'i': m.inc()
            elif action == 'd': m.dec()
            elif action == 'c': m.clear()
            elif action == 'v': print('  value =', m.value())
            elif action == 'm': print('  modulus =', m.modulus())
            elif action == 'c': m.clear()
            elif action == '_': print('  str =',m)
            elif action == '.': exec(prompt.for_string('  Enter command to exec (instance=m)'))
            elif action == 'q': break
            else: print('  Unknown command')
        except AssertionError as report:
            print('  AssertionError exception caught:', report)
        except Exception as report:
            import traceback
            traceback.print_exc()
    print('\nFinished testing Modular')