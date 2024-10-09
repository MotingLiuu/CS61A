def count(s, value):
    '''count the number of occurences of value in sequence s'''
    total = 0
    for ele in s:
        if ele == value:
            total += 1
    return total

odds = [1, 3, 5, 7, 9]
eg1 = [x + 1 for x in odds]
eg2 = [x for x in odds if 25 % x == 0]

def divisor(n):
    return [x for x in range(2, n) if n % x == 0] + [1]

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisor(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def mul(x, y):
    return x * y

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

from operator import add

def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

apply_to_all = lambda map_fn, s: list(map(map_fn, s))
keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

from functools import reduce
from operator import mul

def product(s):
    return reduce(mul, s)

digits = [1, 8, 2, 8]

city = 'Berkeley'

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches mush be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
    
def is_leaf(tree):
    return not branches(tree)

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])

def fib_tree(n):
    if n == 0 or n == 1:
        return [n]
    else:
        left, right = fib_tree(n - 1), fib_tree(n - 2)
        return tree(left[0] + right[0], [left, right])
    
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(tree)])
    
def partition_tree(n, m):
    '''return a partition tree of n using parts of up to m'''
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        return tree(m, [partition_tree(n - m, m), partition_tree(n, m - 1)])
    
def print_parts(tree, partitions = []):
    if is_leaf(tree):
        if label(tree):
            print('+'.join(map(str, partitions)))
        else:
            return
    else:
        print_parts(tree[1], partitions + [label(tree)])
        print_parts(tree[2], partitions)
        
def right_binarize(cb_tree):
    '''Construct a right-branching binary tree
    >>> right_binarize([1, 2, 3, 4, 5, 6, 7])
    [1, [2, [3, [4, [5, [6, 7]]]]]]
    '''
    if not isinstance(cb_tree, list) or len(cb_tree) == 1:
        return cb_tree
    if len(cb_tree) > 2:
        cb_tree = [cb_tree[0], cb_tree[1:]]
    return [right_binarize(b) for b in cb_tree]
