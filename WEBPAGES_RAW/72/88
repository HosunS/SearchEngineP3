import prompt,traceback,math
from goody import irange, type_as_str

default_file_name              = "bsc.txt"
default_separator              = '-->'
default_show_comment           = True
default_show_all               = False
default_show_traceback         = False
default_show_exception         = False
default_show_exception_message = False

def num_just(x):
    return str(x).rjust(5)


# batch_test reads/processes every command in a file (automating the user entering
#   these commands in the console). All exceptions are handled/traced.

def batch_test(file_name,confirm=False):
    print('Starting batch_test')
    local = locals()
    globl = globals()
    for command in open(file_name,'r'):
        try:
            command = command.rstrip()
            print('\nCommand:',command)
            if confirm:
                prompt.for_string('Press enter to do command','')
            exec(command,globl,local)
        except Exception:
            traceback.print_exc()
    print('\nDone batch_test\n')


# batch_self_check reads/processes every test in a file. There are five forms
#  #/comment :  print it
#  c/command  : execute command
#                 (fail on exception)
#  e/evaluate : evaluate expression
#                 (fail on exception or != optional expected result )
#  ^/exception: execute command with expectation of exception
#                 (fail on no exception or wrong exception name -* means all names OK)
#  relop      : evaluate left relop right
#                 (fail on exception or relational operator returns False)


def batch_self_check(file_name=None,\
                     seperator=None,\
                     show_comment=None,\
                     show_all=None,\
                     show_traceback=None,\
                     show_exception=None,\
                     show_exception_message=None,
                     TA_info=None):
    print('Starting batch_self_check')
    if file_name == None:
       file_name = default_file_name
    if seperator == None:
       seperator = default_separator
    if show_comment == None:
       show_comment = default_show_comment
    if show_all == None:
       show_all=default_show_all
    if show_traceback == None:
       show_traceback = default_show_traceback
    if show_exception == None:
       show_exception = default_show_exception
    if show_exception_message == None:
       show_exception_message = default_show_exception_message
    check_num, correct_count, wrong_count, wrong = 0, 0, 0, []
    
    # Use local for local names, to allow exec to add new locals
    #   and change existing ones: see the use of local in local['...'] = ...
    #   and as a third parameter to exec/eval
    local = locals()
    globl = globals()
    for line in open(file_name):
        line = line.rstrip()
        check_num += 1
        try: 
            # Process blank lines (ignore them)
            if line == '':
                continue
            
            # Process #
            if line[0] == '#':
                if local['show_comment']:
                    print(num_just(check_num),line)
                continue
            
            if local['show_all']:
                print(num_just(check_num),line)
            
            # Unpack command
            command = line.split(seperator)
            kind    = command[0]
            
            # Process Command
            if kind =='c' and len(command) == 2:
                to_compute = command[1]
                exec(to_compute,globl)
                correct_count += 1
                
            # Process Query/Expression
            elif kind == 'e'and len(command) == 3:
                to_compute,correct = command[1:3]
 #KLUDGE: if local here, and next has local: size+len+iter problems
                computed = str(eval(to_compute,globl,local))
                if correct != '':
                    if computed == correct:
                        correct_count += 1
                    else:
                        wrong_count += 1
                        wrong.append(check_num)
                        print(num_just(check_num),'*Error:',to_compute,'->',computed,'but should ->',correct)

            # Process Command with expected Exception
            elif kind == '^' and len(command) == 3:
                to_compute,correct = command[1:3]
                try:
 #KLUDGE: must remove local: iter          failure if local here and not local above
 #                           size_len+iter failure if local here and local above
                    exec(to_compute,globl)

                    wrong_count += 1
                    wrong.append(check_num)
                    print(num_just(check_num),'*Error:',to_compute,'failed to raise exception'+('' if correct=='*' else ' from list: '+correct))
                except Exception as exc:
                    # KLUGE for pnamedtuple testing: correct += ',OSError' if correct != '*' else ''
                    if correct == '*' or any([isinstance(exc,eval(e,globl)) for e in correct.split(',')]): #KLUDGE: removed local
                        correct_count += 1
                        if local['show_exception']:
                            print(num_just(check_num),'+Right: Raised correct exception('+type_as_str(exc)+')')
                            if local['show_exception_message']:
                                print(13*' ','Message:',exc)
                    else:
                        wrong_count += 1
                        wrong.append(check_num)
                        print(num_just(check_num),'*Error:',to_compute,'raised wrong exception('+type_as_str(exc)+') should be from list:',correct)
                        if local['show_exception_message']:
                            print(13*' ','Message:',exc)
                        
            # Process Relational Operator
            elif kind in ['==','!=','<','>','<=','>=','in','not in'] and len(command) == 3:
                to_compute,correct = command[1:3]
                try:
                    local['left']  = None
                    local['right'] = None
                    local['left']  = eval(to_compute,globl,local) #KLUDGE: must be local
                    local['right'] = eval(correct,globl,local)
                    if eval('(left)'+kind+'(right)',globl,local):
                        correct_count += 1
                    else:
                        wrong_count += 1
                        wrong.append(check_num)
                        print(num_just(check_num),'*Error: Failed',to_compute,kind,correct)
                        print(9*' ','evaluated:',local['left'],kind,local['right'])
                except:
                    wrong_count += 1
                    wrong.append(check_num)
                    if local['left'] is None:
                        print(num_just(check_num),'*Error:',to_compute,'raised exception; unevaluated: '+correct)
                    elif local['right'] is None:
                        print(num_just(check_num),'*Error:',correct,'raised exception')
                    else:
                        print(num_just(check_num),'*Error:',kind,'raised exception')
                    if local['show_traceback']:
                        traceback.print_exc()
                    

            # Echo Unknown/Malformed Command line
            else:
                print(num_just(check_num),'Unknown/Malformed Command:',line)

        except Exception as e:
            wrong_count += 1
            wrong.append(check_num)
            print(num_just(check_num),'*Error:',to_compute,'raised exception '+type_as_str(e)+': '+str(e))
            if local['show_traceback']:
                traceback.print_exc()
    print('Done batch_self_check:',correct_count,'correct;',wrong_count,'incorrect')
    print('Failed checks:',wrong)

    # For TAs Grading
    if TA_info:
#         commented out to match new test_runner: no more copy/past
#         print('Column analysis (copy and paste line below excluding END)')
        column = []
        for spec in TA_info:
            count = 0
            for w in wrong:
                if w in spec:
                    count += 1
            column.append(count)
        print('\t'.join([str(-c) if c > 0 else '' for c in column]))
#         print('-->'+'\t'.join([str(-c) if c > 0 else '' for c in column])+'<--')
#         print('Done with column analysis')




# Driver: prompts and executes commands (including calling the methods above)
# ! means call batch_self_check() with all arguments defaulted
# ? means call batch_self_check() prompting for all arguments
#    (with standard default values)

def driver():
    global default_file_name,default_separator,default_show_comment,\
           default_show_all,default_show_traceback,default_show_exception,\
           default_show_exception_message
    local = locals()
    globl = globals()
    print('Driver started')
    old = '!'
    while True:
        try:
            old = prompt.for_string('Command',default=old)
            if old == 'quit':
                print('Driver stopped')
                return None
            if old == '!':
                batch_self_check()
            elif old == '?':
                default_file_name              = prompt.for_string('file_name             ',default_file_name)
                default_separator              = prompt.for_string('separator             ',default_separator)
                default_show_comment           = prompt.for_bool  ('show_comment          ',default_show_comment)
                default_show_all               = prompt.for_bool  ('show_all              ',default_show_all)
                default_show_traceback         = prompt.for_bool  ('show_traceback        ',default_show_traceback)
                default_show_exception         = prompt.for_bool  ('show_exception        ',default_show_exception)
                default_show_exception_message = prompt.for_bool  ('show_exception_message',default_show_exception_message)
                batch_self_check()
                old = '!'
            else:
                exec(old,local,globl)
            print()
        except Exception:
            traceback.print_exc()
            print()
