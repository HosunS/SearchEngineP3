"""
Module with prompting functions
Use as 
  import prompt
  ... prompt.for_int(...)
"""


from goody import leading

def for_value(prompt_text, convert=(lambda x : x), is_legal=(lambda x : True), default=None, error_message='reenter'):
    """
    Prompt for value using the specified prompt_text (with default in brackets
      appended if it is non-None) followed by ': '; convert the entered value
      (or use the default if the user just presses enter), ensure is_legal
      returns True when called on it, and return that value.
    Display error_messages for all possible failures
    See the comments in the code for more details
    See the calls to for_value below, for examples of how it is called.
    """
    while True:
        try:
            #display answer (and default, if supplied) and ': '; read str that is user's answer
            response = input(prompt_text + ('['+str(default)+']' if default != None else '') + ': ')

            #if there is no answer, and no default, print error message and reprompt
            #kludge: so the user cannot enter an empty string unless the empty string is a default!
            if len(response) == 0 and default == None: 
                print(leading(prompt_text,extra=2)+'Must enter a value: there is no default')
                continue
            
            #set answer to either be the default (if there is no answer) or convert the user's answer
            #see except clause, in case conversion fails: e.g., int('abc') throws an exception
            answer = default if len(response) == 0 and default != None else convert(response) 
            
            #if the answer (default or user's) is legal, return it, other print the error message
            if is_legal(answer):
                return answer
            else:
                print(leading(prompt_text,extra=2)+'Entry Error:',"'"+str(answer)+"'; ",error_message)
        #if conversion raises an exception, print an error message and reprompt
        except Exception as x:
            print(leading(prompt_text,extra=2)+'Exception:',x)
            print(leading(prompt_text,extra=2)+'Possible error: cannot convert str \'',response,'\' to specified type of value',sep='')


def for_int(prompt_text, default=None, is_legal=(lambda x : True), error_message='not a legal value'):
    """
    Prompt for an int; use the specified prompt_text (with default in brackets
      appended if it is non-None) followed by ': '; verify that the entered value
      (using default if the user just presses enter) is an int and is_legal
      returns True when called on it (and if not display the error_message)
    See the call to for_value below, and the documentation and code for for_value above.
    """
    lead = leading(prompt_text,extra=2)
    return for_value(prompt_text, int, (lambda x: type(x) is int and is_legal(x)), default, error_message+':\n'+lead+'Please enter a legal value')
 
    
def for_float(prompt_text, default=None, is_legal=(lambda x : True), error_message='not a legal value'):
    """
    Prompt for a float; use the specified prompt_text (with default in brackets
      appended if it is non-None) followed by ': '; verify that the entered value
      (using default if the user just presses enter) is a float and is_legal
      returns True when called on it (and if not display the error_message)
    See the call to for_value below, and the documentation and code for for_value above.
    """
    lead = leading(prompt_text,extra=2)
    return for_value(prompt_text, float, (lambda x: type(x) is float and is_legal(x)), default, error_message+':\n'+lead+'Please enter a legal value')

    
def for_num(prompt_text, default=None, is_legal=(lambda x : True), error_message='not a legal value'):
    """
    Prompt for an int or float; use the specified prompt_text (with default in brackets
      appended if it is non-None) followed by ': '; verify that the entered value
      (using default if the user just presses enter) is an int or float and is_legal
      returns True when called on it (and if not display the error_message)
    See the call to for_value below, and the documentation and code for for_value above.
    """
    lead = leading(prompt_text,extra=2)
    return for_value(prompt_text, eval, (lambda x: (type(x) is int or type(x) is float) and is_legal(x)), default, error_message+':\n'+lead+'Please enter a legal number')

    
def for_int_between(prompt_text, low, high, default=None, error_message=''):
    lead = leading(prompt_text,extra=2)
    return for_value(prompt_text+'('+str(low)+'..'+str(high)+')',
                    int, (lambda x: type(x) is int and low<=x<=high), default, error_message+'\n'+lead+'Please enter a value in the range ['+str(low)+','+str(high)+']')
    """
    Prompt for an int; use the specified prompt_text (with low and high in parentheses
      appended and default in brackets appended if it is non-None) followed by ': ';
      verify that the entered value (using default if the user just presses enter) is an
      int and it is in the range low to high inclusive (and if not display the error_message)
    See the call to for_value below, and the documentation and code for for_value above.
    """


def for_string(prompt_text, default=None, is_legal=(lambda x : True), error_message=''):
    """
    Prompt for a string; use the specified prompt_text (with default in brackets
      appended if it is non-None) followed by ': '; verify that the entered value
      (using default if the user just presses enter) returns True when is_legal is
      called on it (and if not display the error_message)
    See the call to for_value below, and the documentation and code for for_value above.
    """
    lead = leading(prompt_text,extra=2)
    return for_value(prompt_text, (lambda x : x), is_legal, default, error_message+'\n'+lead+'Please enter a legal String')


def for_char(prompt_text, default=None, legal=None, error_message='Please enter one char in the range (if specified)'):
    lead = leading(prompt_text,extra=2)
    return for_value(prompt_text+('('+legal+')' if legal != None else ''),
                    (lambda x : x[0]), (lambda x: x in legal) if legal != None else (lambda x : True), default,
                    error_message+('\n'+lead+'Please enter one of ' + legal if legal != None else ''))
    """
    Prompt for a char; use the specified prompt_text (with legal in parentheses
      appended and default in brackets appended if it is non-None) followed by ': ';
      verify that the entered value (using default if the user just presses enter) is
      one of the chars in legal (and if not display the error_message)
    Note that if if the user enters a multiple-char string, only the first char is processed
    See the call to for_value below, and the documentation and code for for_value above.
    """
 

def for_bool(prompt_text, default=None, error_message='Please enter a bool value: True or False'):
    """
    Prompt for a bool; use the specified prompt_text (with default in brackets
      appended if it is non-None) followed by ': '; verify that the entered value (using
      default if the user just presses enter) is True or False (and if not display the
      error_message)
    See the call to for_value below, and the documentation and code for for_value above.
    """
    return for_value(prompt_text, (lambda x : True if x == 'True' else False if x == 'False' else None), (lambda x: type(x) is bool), default, error_message)


def for_string_via_index(prompt_text, default=None, legal=None, error_message='Please enter a legal integer index'):
    """
    Prompt for an int index but return its associated string; use the specified prompt_text
      (with each string in the list legal prefaced by its index in brackets, and with default
      in brackets appended if it is non-None) followed by ': '; verify that the entered value
      is the index of some string (or just return the default if the user just presses enter)
      (and if not display theerror_message)
    See the call to for_value below, and the documentation and code for for_value above.
    """
    prompt_text += '('+', '.join(['['+str(x)+']'+t for x,t in zip(range(0,len(legal)),legal)]) +')'
    return for_value(prompt_text,
                 (lambda x : legal[int(x)] if 0<=int(x)<len(legal) else None ),
                 (lambda x : x in legal),
                 default,
                 error_message='Enter an int 0-'+str(len(legal)-1)+('(or press enter for the default)' if default != None else "")
              )   

            
if __name__ == '__main__':
    print('Begin testing prompt module') 
    command_prompt = \
"""\nTesting prompt module:     Queries         Other
  . - exec(...)
  f _ for_
  q _ quit
                 
Command""" 
    while True:
        action = for_char(command_prompt, legal='.fq')
        try:
            if   action == '.': exec(for_string('  Enter command to exec'))
            elif action == 'f': 
                value = eval('for_'+input('Enter call: for_'))
                print('prompt returned value =',value)
            elif action == 'q': break
            else: print('  Unknown command')
        except AssertionError as report:
            print('  AssertionError exception caught:', report)
        except Exception as report:
            import traceback
            traceback.print_exc()
    print('\nFinished testing prompt module')
