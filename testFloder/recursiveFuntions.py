def sum_digits(n):
    '''Compute the sum of digits of a int number
    
    n: an int number
    
    >>> sum_digits(11408855402054064613470328848384)
    126
    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    '''
    if n // 10 == 0:
        return n
    else:
        return sum_digits(n // 10) + n % 10

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

def is_even(n):
    if n == 0:
        return True
    else:
        if n == 1:
            return False
        else:
            return is_even(n - 2)
        
def cascade(n):
    '''Print a cascade of prefixes of n
    
    >>> cascade(123)
    123
    12
    1
    12
    123
    >>> cascade(6429)
    6429
    642
    64
    6
    64
    642
    6429
    '''
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
        
def play_alice(n):
    '''
    >>> play_alice(20)
    Bob wins the game
    '''
    if n == 1:
        print('Alice wins the game')
    else:
        play_bob(n - 1)
        
def play_bob(n):
    if n == 1:
        print('Bob wins the game')
    else:
        if n % 2 == 0:
            play_alice(n - 2)
        else:
            play_alice(n - 1)
            
def fib(n):
    '''Compute the nth fib number
    >>> fib(6)
    5
    >>> fib(7)
    8
    '''
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def count_partitions(n, m):
    '''Compute the number of different partitions of n using parts up to m
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    '''
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0:
        return 0
    if m == 1:
        return 1
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)