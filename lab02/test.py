def sum_digits(n):
    '''Return the sum of the digits of n
    >>> sum_digits(10)
    1
    >>> sum_digits(555)
    15
    '''
    result = 0
    
    while n > 0:
        result += n % 10
        n = n // 10
    return result
    
    
def count_fives(n):
    '''Return the number of values i from 1 to n (including n)
    where sum_digits(n * i) is 5.
    >>> count_fives(10) # Among 10, 20, 30, ..., 100, only 50 (10 * 5) has digit sum 5
    1
    >>> count_fives(50) # 50, 500, 1400, 2300
    4
    '''
    count, i = 0, 1
    
    while i <= n:
        if sum_digits(n * i) == 5:
            count += 1
        i += 1
    
    return count

def is_prime(n):
    '''Return True if n is a prime number, return False if not
    >>> is_prime(13)
    True
    >>> is_prime(27)
    False
    '''
    i = 2
    
    while i < n:
        if n % i == 0:
            return False
        i += 1
    
    return True

def count_primes(n):
    '''Return the number of prime numbers up to and including n
    >>> count_primes(6) #2, 3, 5
    3
    >>> count_primes(13) #2, 3, 5, 7, 11, 13
    6
    '''
    count, i = 0, 2
    
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
        
    return count

def count_cond(condition):
    '''Returns a function with one parameter N that counts all the numbers from 1 to N
    that satisfy the two-argument predicate function Condition, where the first argument
    for Condition is N and the second argument is the number from 1 to N
    
    condition -- two-argument predicate function takes in two number N, i
    
    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10) # 50(10 *5)
    1
    >>> count_fives(50) # 50, 500, 1400, 2300
    4
    '''
    def counter(n):
        count, i = 0, 1
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    
    return counter