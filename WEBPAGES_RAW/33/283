import random


class Dice:
    """
    Models an ensemble of dice: >= 1 dice, with each die having >= 1 sides.
    Dice in the ensemble can have different numbers of sides.
    All the dice can be rolled, their pips (and pip sum) can be queried.
    """
    def __init__(self,max_pips):
        """
        Instantiate like Dice([6,6]) for 2 six-sided dice
        Dice instance is unrolled (many operations require dice to be rolled first).
        
        Args:
            max_pips: a list of positive (>=1) integers
            
        Returns:
            A Dice instance with len(max_pips) dice, the ith of which
              has maxPip[i] sides, which has been rolled 0 times.
        """
        assert len(max_pips) >= 1, 'Dice.__init__: max_pips is empty'
        for i in range(0,len(max_pips)):
            p = max_pips[i]
            assert p >= 1, 'Dice.__init__: max_pips['+str(i)+']='+str(p)+': must be an int >= 1'
        self._max_pips   = max_pips[:]       #Copy to avoid aliasing
        self._pips      = [0]*len(max_pips)
        self._roll_count = 0

    def roll(self):
        """
        Returns the dice ensemble after rolling every die in it.
        Allows cascaded calls: d.roll().pip_sum()
        """
        self._roll_count += 1
        self._pips = [ random.randint(1,max_pips) for max_pips in self._max_pips ]
        #for i in range(0,len(self._pips)):
        #  self._pips[i] = random.randint(1,self._max_pips[i])
        return self


    def number_of_dice(self):
        """
        Returns the number of dice in the ensemble (>= 1).
        """
        return len(self._pips)


    def all_pip_maximums(self):
        """
        Returns a list of the maximum pips for each die.
        """
        return self._max_pips[:]


    def rolls(self):
        """
        Returns the number of times the dice have been rolled (>=0).
        """
        return self._roll_count


    def pips_on(self,i):
        """
        Returns the number of pips showing in die i (first die is i = 0).
        """
        assert self._roll_count > 0, 'Dice.pips_on: dice not rolled' 
        assert 0<= i < len(self._pips), \
          'Dice.pips: die index i('+str(i)+') must be >= 0 and <'+str(len(self._pips))
        return self._pips[i]


    def all_pips(self):
        """
        Returns a list of all pips showing.
        Note: d.all_pips()[i] == d.pips_on(i)
        """
        return self._pips[:]


    def pip_sum(self):
        """
        Returns the sum of the pips showing on all the dice.
        """
        assert self._roll_count > 0, 'Dice.pip_sum: dice not rolled' 
        return sum(self._pips)

        
    def pips_same(self):
        """
        Returns whether or not all die show the same number of pips.
        For 2 dice, asking pips_same is the same as asking doubles. 
        """
        return all( [self._pips[0] == p for p in self._pips] )

    
    def __str__(self):
        """
        Return dice as a str
        Returns a string representation for a Dice, such that
        d2 = eval(str(d)) copies the state of d
        """
        return 'Dice('+str(self._max_pips)+')'

    
    def standard_rolls_for_debugging(self):
        """
        Returns None
        Seeds the random number generator so that the same sequence of
          rolls will occur, which allows for debugging of the same
          'random' throws
        """
        random.seed(12161949)


 
 
        
if __name__ == '__main__': 
    import prompt
    print('Begin testing Dice') 
    command_prompt = \
"""\nTesting Dice:
Commands     Queries                  Other
  r - roll     n - number_of_dice       . - exec(...)
               m - all_pip_maximums     D - standard_rolls_for_debugging
               s - rolls                q - quit
               o - pips_on
               a - all_pips
               ? - pip_sum
               =  - pips_same
               _  - __str__
Command"""                            
    d = Dice(eval(prompt.for_string('Enter list of max pips', default='[6,6]')))
    while True:
        action = prompt.for_char(command_prompt, legal='rnmsoa?=_.Dq')
        try:
            if   action == 'r': d.roll()
            elif action == 'n': print('  Number of dice =',d.number_of_dice())
            elif action == 'm': print('  all pip maximums =',d.all_pip_maximums())
            elif action == 's': print('  rolls =',d.rolls())
            elif action == 'o':
                i = prompt.for_int_between('  Enter die #', 0, d.number_of_dice()-1)
                print('  pips on die #',str(i),' =',d.pips_on(i))
            elif action == 'a': print('  all pips =',d.all_pips())
            elif action == '?': print('  pip sum =',d.pip_sum())
            elif action == '=': print('  pips all the same =',d.pips_same())
            elif action == '_': print('  str =',str(d))
            elif action == '.': exec(prompt.for_string('  Enter command to exec (instance=d)'))
            elif action == 'D': d.standard_rolls_for_debugging()
            elif action == 'q': break
            else: print('  Unknown command')
        except AssertionError as report:
            print('  AssertionError exception caught:', report)
        except Exception as report:
            import traceback
            traceback.print_exc()
    print('\nFinished testing Dice')