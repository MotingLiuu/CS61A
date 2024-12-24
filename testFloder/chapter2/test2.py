def hailstone(n):
    """
    Yields the elements of the hailstone sequence starting at n.
    At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    if n % 2 == 0:
      yield from hailstone(n // 2)
    else:
      yield from hailstone(3 * n + 1)

def stair_ways(n):
    """
    Yield all the ways to climb a set of n stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> list(s_w) # Ensure you're not yielding extra
    []
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
      yield [1]
    elif n == 2:
      yield [1, 1]
      yield [2]
    else:
      for way in stair_ways(n - 1):
        yield [1] + way
      for way in stair_ways(n - 2):
        yield [2] + way
        
print([way for way in stair_ways(4)])