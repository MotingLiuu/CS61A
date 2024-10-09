empty = 'empty'

def is_link(s):
    '''s is a linked list if it is empty or a (first, rest) pair'''
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    '''construct a linked list from its first element and the rest'''
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    '''return the first element of a linked list s'''
    assert is_link(s), 'first only applies to linked lists'
    assert s != empty, 'empty linked list has no first element'
    return s[0]

def rest(s):
    '''return the rest of the elements of a linked list s'''
    assert is_link(s), 'rest only applies to linked lists'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def len_link(s):
    '''return the length of linked list s
    >>> len_link(link(1, link(2, link(3, link(4, empty)))))
    4
    '''
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    '''Return the element at index i of linked list s
    >>> getitem_link(link(1, link(2, link(3, link(4, empty)))), 1)
    2
    '''
    while i > 0:
        s, i = rest(s), i - 1
        return first(s)

def len_link_recursive(s):
    '''return the length of a linked list s
    >>> len_link_recursive(link(1, link(2, link(3, link(4, empty)))))
    4
    '''
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    '''return the element at index i of linked list s
    >>> getitem_link_recursive(link(1, link(2, link(3, link(4, empty)))), 1)
    2
    '''
    if i == 0:
        return first(s)
    else:
        return getitem_link_recursive(rest(s), i - 1)
    
def extend_link(s, t):
    '''return a list with the elements of s followed by those of t
    >>> extend_link(four, four)
    [1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
    '''
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))
    
def apply_to_all_link(f, s):
    '''apply f to each elements of s
    >>> apply_to_all_link(lambda x: x * x, four)
    [1, [4, [9, [16, 'empty']]]]
    '''
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))
    
def keep_if_link(f, s):
    '''return a list with elements of s for which f(e) is true
    >>> keep_if_link(lambda x: x%2 == 0, four)
    [2, [4, 'empty']]
    '''
    assert is_link(s)
    if s == empty:
        return s
    else:
        if f(first(s)):
            return link(first(s), keep_if_link(f, rest(s)))
        else:
            return keep_if_link(f, rest(s))

def join_link(s, separator):
    '''return a string of all elements in s separated by separator
    >>> join_link(four, ", ")
    '1, 2, 3, 4'
    '''
    if s == empty:
        return ''
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + str(separator) + join_link(rest(s), separator)\
            
def partitions(n, m):
    '''return a linked list of partitions of n using parts of up to m. Each partition is represented as a linked list'''
    



four = link(1, link(2, link(3, link(4, empty))))