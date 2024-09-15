def make_keeper(n):
    '''Returns a function that takes one parameter cond and print out all integers
    1..i..n where calling cond(i) return True
    
    >>> make_keeper(20)(is_prime)
    2
    3
    5
    7
    11
    13
    17
    19
    '''
    def keeper(cond):
        i = 1
        while i <= n:
            if cond(i) == True:
                print(i)
            i += 1
    
    return keeper

def is_prime(n):
    '''Returns True if n is a prime number, returns False if not
    
    >>> is_prime(13)
    True
    >>> is_prime(27)
    False
    '''
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def find_digit(k):
    '''Returns a function that returns the kth digit of x
    
    >>> find_digit(2)(1234)
    3
    >>> find_digit(5)(123)
    0
    >>> find_digit(6)(12312597394872)
    3
    '''
    def find_kth(x):
        count = 0
        while count < k - 1:
            x = x // 10
            count += 1
        return x % 10
    return find_kth

def match_k(k):
    '''Returns a function that checks if digits k apart match
    
    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(21111111111)
    False
    >>> match_k(3)(123123)
    True
    '''
    def check(x):
        while x // (10 ** k) > 0:
            if x % 10 != x // (10 ** k) % 10:
                return False
            x //= 10
        return True
    
    return check
            