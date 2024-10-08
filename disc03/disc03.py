def swipe(n):
    '''prints the digits of argument n, one per line, first backward then forward
    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    '''
    if n // 10 == 0:
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)
        
def skip_factorial(n):
    '''Return the product of positive integers n*(n-2)*(n-4)*...
    >>> skip_factorial(5)
    15
    >>> skip_factorial(8)
    384
    '''
    if n <= 2:
        return n
    else:
        return n * skip_factorial(n - 2)
    
def is_prime(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        
        i = i + 1
    return True

def is_prime_re(n):
    '''returns True if n is a prime number and False otherwise
    >>> is_prime_re(2)
    True
    >>> is_prime_re(16)
    False
    >>> is_prime_re(521)
    True
    '''
    def check_all(i):
        #Check wether integers between i and n evenly divide n
        if i == n:
            return True
        elif n % i == 0:
            return False
        return check_all(i + 1)
    
    return check_all(2)

def hailstone(n):
    '''Print out the hailstone sequence starting at n, and return the number of elements in the sequence
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    '''
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    elif n % 2 == 1:
        return hailstone(n * 3 + 1) + 1
    
def seven(n: int, k: int) -> None:
    i, flag, player = 1, 1, 0
    
    def next(player, flag):
        if flag == 1:
            return (player + 1) % k
        else:
            return (player - 1) % k
        
    def play(i, n, flag, player):
        print(f'player {player + 1} says {i}')
        if i == n:
            return 
        else:
            if i % 10 == 7 or i % 7 == 0:
                flag = -1 * flag
            play(i + 1, n, flag, next(player, flag))
    
    play(1, n, flag, player)
            