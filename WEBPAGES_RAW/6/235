def is_even        (x): return x%2 == 0
def is_odd         (x): return x%2 == 1
def is_positive    (x): return x > 0
def is_non_negative(x): return x >= 0
def is_percentage  (x): return 0 <= x <= 1

def is_bigger_than (i):
    def is_bt (x): return x > i

def is_less_than (i):
    def is_lt (x): return x < i

def is_prime (x):
    assert type(x) is int and x >= 0, 'predicate.is_prime x is not a positive int: '+str(x)
    if x <= 2:
        return x == 2
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def reverse(p):
    def reverse_it(x):
        return not p(x)
    return reverse_it

def length_equal(i):
    def len_eq(s): return len(s) == i
    return len_eq