# Chapter 2
## 2.4 Mutable Data
Adding state to data is a central ingredient of a paradigm called object-oriented programming.

### 2.4.1 Object Metaphor
Functions: perform operation and data were operated upon. Can be manipulated as data, could also be called to perform computation.

Objects: combine data values with behavior.

### 2.4.2 Sequence Objects
Instance of primitive built-in values such as numbers are immutable. The values themselves cannot change over the course of program execution.

Lists are mutable.
```python
chinese = ['coin', 'string', 'myraid']
suits = chinese
```
这里的suits相当于chinese指向的序列的一个别名。对suits进行更改会影响chinese. The same list object is bound to `suits`
The behavior of mutable data is different from immutable data. With mutable data, methods called on one name can affect another name at the same time.

e.g.
![alt text](image.png)
![](image-1.png)
![alt text](image-2.png)

**Copy**
lists can be copied using `list` constructor function. Changes to one lists do not affect another.
```python
nest = list(suits) # Bind "nest" to a second list with the same elements
nest[0] = suits # Create a nested list
```
In this situation, changing the list referenced by `suits` will affect the nseted list that is the first element of `nest`, but not the other elements.
```python
suits.insert(2, 'Jocker') # Insert an element at index 2, shifting the rest
nest
[['heart', 'diamond', 'Joker', 'spade', 'club'], 'diamond', 'spade', 'club']
```

**test whether two Objects are the same** 
`is` and `is not`, test whether two expressions in fact evaluate to the identical object.
```python
>>> suits is nest[0]
True
>>> suits is ['heart', 'diamond', 'spade', 'club']
False
>>> suits == ['heart', 'diamond', 'spade', 'club']
True
```

**List comprehensions**
List comprehension always creates a new list. `unicodedata` moudule tracks the official names of every character in the Unicode alphabet. 
```python
>>> from unicodedata import lookup
>>> [lookup('WHITE ' + s.upper() + ' SUIT') for s in suits]
['♡', '♢', '♤', '♧']
```

**Tuple**
Built in `tuple` type, is an immutable sequence.
While it is not possible to change which elements are in a tuple, it is possible to change the value of a mutable element contained within a tuple.
![](image-3.png)
也就是说tuple实际上存贮了一个指向对象的指针，不能对tuple存储的指针进行操作，但如果这个指针指向可变数据的话，可以对这个可变数据进行操作。操作后的变化会自然而然反映在tuple上。

**Dictionaries**
Contain key-value pairs, both keys and values are objects. Provide an abstraction for storing and retrieving values that are indexed not by consecutive integers, but by descriptive keys.

```python
>>>numerals = {'I': 1.0, 'V': 5, 'X': 10}
>>>numerals['X']
10
```

A dictionary can have at most one value for each key. Adding new key-value pairs and changing the exsiting value gor a key can both be achieved with assignment statements.
```python
>>>numerals['I'] = 1
>>>numerals['L'] = 1
>>>numerals
{'I': 1, 'X': 10, 'L': 50, 'V': 5}
```
Dictionaries are unodered collections of key-value pairs.

Dictionary type also supports various methods of iterating over the contents of the dictionary as a whole. `keys`, `values`, `items` all return iterable values.
```python
>>>sum(numerals.values())
66
```
A list of key-value pairs can be converted into dictionary by calling the `dict` constructor function
```python
>>> dict([(3, 9), (4, 16), (5, 25)])
{3: 9, 4: 16, 5: 25}
```

Restrictions:
1. key of dictionary cannot be or contain a mutable value
2. can be at most one value for a given key

**get()** returns either the value for a key, if the key is present, or a default value.
```python
>>>numerals.get('A', 0)
0
>>>numerals.get('V', 0)
5
```

**Dictionary comprehension** 
A key expression and a value expression are separated by a colon
```python
>>> {x: x*x for x in range(3, 6)}
{3: 9, 4: 16, 5: 25}
```

### 2.4.4 Local State
**local state** are changing values that have some particular contents at any point in the execution of a program.

Functions can also have local state.
```python
>>> withdraw(25)
75
>>> withdraw(25)
50
>>> withdraw(60)
'Insufficient funds'
>>> withdraw(15)
35
```
`withdraw()` must be created with an initial account balance. `make_withdraw()`, a higher-order function, takes a starting balace as an argument to create `withdraw()`

```python
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
```

The `nonlocal` statement declares that whenever we change the binding of the name `balance`, the binding is changed in the first frame in which `balance` is already bound.
将balance声明为nonlocal之后，每当nonlocal的值发生变化，都会向之前的帧进行查找，所有的变化都会更新到`balance`第一次被声明的位置。在这个情况下，`balance`第一次在`make_withdraw()`的参数的位置被声明。所以在`withdraw()`函数中balance的变化会同步更新到`make_withdraw()`中的`balance`

![alt text](image-5.png)
![alt text](image-4.png)
首先在global中运行`make_withdraw()`函数，进入其frame
![alt text](image-6.png)
在frame中声明`balance`，并将其bind到20. 接着将`withdraw`和`return value`bind到函数object上。
![](image-7.png)
返回Global的frame中，接着将`wd` bind 到返回值所指的object上
![alt text](image-8.png)
进入到f1，之后进入f2的frame中
![alt text](image-9.png)
这里对balance的更改也会影响到`make_withdraw()`中的`balance`

python中赋值时隐式声明变量，无需单独操作。对于赋值时如果object是不可变类型，赋值操作会创建一个新的对象，并将变量名重新绑定到这个新的对象。 如果是可变类型，则会直接修改原对象。
使用nonlocal来声明一个变量的时候，python会从当前函数的外层作用域开始，向上逐层查找哪个作用域中已经定义了`balance`，当找到一个作用域中已经绑定了`balance`，这个作用于就是first frame。这个frame中的`balance`的绑定会被改变。也就是说nonlocal声明的变量，视作向上逐frame查找，找到的含有这个变量的第一个frame中的变量。

```python
def make_withdraw(balance):
    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

wd = make_withdraw(20)
wd(5)
```
这个函数报错的原因是因为存在`balance = balance - amount`这行代码，python会在执行代码之前根据代码结构来确定一个变量是否为局部变量。在函数编译阶段完成。
如果去掉这行代码
```python
def make_withdraw(balance):
    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds'
        return balance
    return withdraw

wd = make_withdraw(20)
wd(5)
```
这样就不会报错

python has an unusual restriction regarding the lookup of names: within the body of a function, all instances of a name must refer to the same frame(多次出现的同一个变量名必须指向同一个frame). As a result, Python cannot look up the value of a name in a non-local frame, then bind that same name in the local frame, because the same name would be accessed in two different frames in the same function. This restriction allows Python to precompute which frame contains each name before executing the body of a function. When this restriction is violated, a confusing error message results.

This `UnboundLocalError` appears because `balance` is assigned locally in line 5, and so Python assumes that all references to `balance` must appear in the local frame as well. This error occurs before line 5 is ever executed, implying that Python has considered line 5 in some way before executing line 3. As we study interpreter design, we will see that pre-computing facts about a function body before executing it is quite common. In this case, Python's pre-processing restricted the frame in which `balance` could appear, and thus prevented the name from being found. Adding a `nonlocal` statement corrects this error. The `nonlocal` statement did not exist in Python 2.

```python
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

wd = make_withdraw(20)
wd(5)
```
这样就不会报错，表明balance存在于上一个frame。

### 2.4.5 The Benefits of Non-Local Assignment
Only `wd` is associated with the frame for `make_withdraw` in which it was defined. If `make_withdraw` is called again, then it will create a seperate frame with a seperate binding for `balance`. A second call to `make_withdraw` returns a second `withdraw` function that has a different parent.

### 2.4.6 The Cost of Non-Local Assignment
When two names `wd` and `wd2` are both bound to a `withdraw` function, it does matter whether they are bound to the same function or different instance of that function.
![alt text](image-10.png)
In this case, calling the function named by `wd2` changed the value of the function named by `wd`, because both names refer to the same function.

Only function calls can introduce new frames. Assignment statements always change bindings in existing frames. In this case, unless `make_withdraw` is called twice, there can be only one binding for `balance`

纯函数是**不依赖于或改变非局部环境**的函数
* 函数的输出完全由输入决定，且函数调用不会产生改变其他函数，或者环境的副作用
* 如果一个表达式只包含纯函数，它是**引用透明**的，即
    * 如果用一个子表达式的值替换它本身，表达式的值不会发生变化
    * `2+3`始终等于`5`。用`5`替换`2+3`并不会改变程序
引入非纯函数会破坏这种透明性


### 2.4.7 Implementing Lists and Dictionaries
Represent mutable list using functions with local state.
Represent a mutable linked list by function that has a linked as its local state.

The function is a dispatch function and its arguments are first a message, followed by additional arguments to parameterize that method. This message determines the behavior of the function, and the additional arguments are used in that behavior.

Mutuable list will respond to five different message: `len`, `getitem`, `pop_first`, and `str`.

```python
def mutable_link():
    '''return a functional implementation of a mutable linked list.'''
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ',')
    return dispatch
```
Construct a functionally implemented linked list by adding each element in reverse order.
```python
def to_mutable_link(source):
    '''返回一个与源列表相同内容的函数列表'''
    s = mutable_link()
    for element in reversed(source):
        s('push_first', element)
    return s
```
Construct a functionally implemented mutable linked lists.
```python
>>> s = to_mutable_link(suits)
>>> type(s)
<class 'function'>
>>> print(s('str'))
heart, diamond, spade, club
```

**Implementing Dictionaries**
```python
def dictionary():
    
    records = []
    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch
```
```python
my_dict = dictionary()
my_dict('setitem', key='LIU', value=23)
my_dict('setitem', key='WANG', value=21)
>>>my_dict('getitem', key='LIU')
23
```

### Dispatch Dictionaries
look up a message using dictionaries.
```python
def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit': deposit,
                'withdraw': withdraw,
                'balance': initial_balance
                }
    return dispatch
```
```python
def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']
```
```python
a = account(20)
deposit(a, 5)
withdraw(a, 17)
check_balance(a)
```

### 2.4.9 Propagating Constraints
![](image-12.png)
Constraint System between `Celsius` and `Fahrenheit`
The constrain between `c` and `f` can be thought of as  a network consisting of primitive `adder`, `multiplier` and `constant` constrains.

**Processing Flow**: when a connector is given a value, it awakens all of its associated constrains (expect for the constrain that just awakened it) to inform them taht it has a value. Then each awakened constraint box polls its connectors to see if there is enough information to determine a value for a connector. If so, the box sets that connector, which then awakens all of its associated constrains, and so on.

* **Connectors** are dictionaries that hold a current value and respond to messages that manipulate that value.
* **Constraints** are dictionaries that do not hold local states themselves. Their responses to messages are **non-pure functions** that change the connectors that they constrain.
为什么这个返回值是一个非纯函数，这意味着变量是和函数同级在系统的frame中的吗，还是变量存在于connector中呢。

e.g
send a **message** to connector to set its value.
```python
>>> celsius['set_val']('user', 25)
Celsius = 25
Fahrenheit = 77.0
```
celsius是一个connector，其中包含了一个dispatch dictionary。`'set_val'`对应的value是一个函数？ 那么constraint的返回值到底是什么？
```python
>>> fahrenheit['set_val']('user', 212)
Contradiction detected: 77.0 vs 212
```
tell `celsius` to forget its old value to reuse the network with new values.
```python
>>> celsius['forget']('user')
Celsius is forgotten
Fahrenheit is forgotten
```

**Implementing the Constraint System**
**Connector**
dictionaries that map message names to function and data values.
* `connector['set_val'](source, value)` indicates that the `source` is requesting the connector to set its current value to `value`
* `connector['has_val']()` returns whether the connector already has a value.
* `connecotr['val']` is the current value of the connector
* `connector['forget'](source)` tells the connector that the `source` is requesting it to forget its value.
* `connector['connect'](source)` tells the connector to participate in a new constraint, the `source`

**Constraint**
dictionaries, which receive information from connectors by means of two message
* `constraint['new_val']()` indicates that some connector that is connected to the constraint has a new value.
* `constraint['forget']()` indicates that some connector that is connected to the constraint has forgotten its value.

`adder` function:
to support multidirectional constraint propagation, the adder must also specify that it subtracts `a` from `c` to get `b` and likewise subtracts `b` from `c` to get `a`
```python
>>> from operator import add, sub
>>> def adder(a, b, c):
        return make_ternary_constraint(a, b, c, add, sub, sub)
```
The implementation of a generic tenary(three-way) constraint, which uses the three connectors and three functions from `adder` to create a constraint that accepts `new_val` and `forget` messages. The response to messages are local functions, which are placed in a dictionary called `constraint`
```python
def make_ternary_constarint(a, b, c, ab, ca, cb):
    '''The constraint that ab(a, b)=c and ca(c, a)=b and cb(c, b)=a'''
    def new_value():
        av, bv, cv = [connector['has_val']() for  connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

def adder(a, b, c):
    '''The constraint that a + b = c'''
    return make_ternary_constarint(a, b, c, add, sub, sub)
```
the dictionary called `constraint` is a dispatch dictionary. It responds to the two messages that constraints receive, is also passed as the `source` argument in calls to its connectors.

The constraint's local function `new_value` is called whenever the constraint is informed that one of its connectors has a value. If the constraint is informed that one of its connectors has forgotten its value, it requests that all of its connectors now forget their values.

**Representing connectors** A connector is represented as a dictionary that contains a value, but also has response functions with local state. the connector must track the `informant` that gave it its current value, and a list of `constraints` in which it participates.
```python
    '''A connector between constraints'''
    informant = None
    constraints = []
    
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_expect(source, 'new_val', constraints)
        else:
            if val != value:
                print('Constradiction detected:', val, 'vs', value)
    
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_expect(source, 'forget', constraints)
    
    connector = {'val':  None,
                 'set_val':  set_value,
                 'forget':  forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)
                 }
    return connector
```
注意到整个connector包含一个调度字典connector，其中包含了一个值和4种方法，设置，遗忘，检查是否有值，连接到一个constraint上。
还有一个三个值，name用来记录connector的名字，informant用来记录消息的来源，constraints用来记录连接的constraint

整理：
1. **connector**： have a dispatch dictionary(connector) and a list used to record the constraints connecting to and a string informant to save the source of the message.
When `set_value` or `forget_value` is called, the connector will process as they are telled, then inform the constraints connecting to the change. And so on.
2. **make_ternary_constraint(a, b, c, ab, ca, cb)**: have a dispatch dictionary and two functions with local state(the connector connecting to). When get `new_val` the `new_value()` will be called, When get `forget` the `forget_value()` will be called. The connector connecting to will be add when construct a constraint.
3. **constant(connector, value)**: 只有一个操作，就是在创建的时候将connector的值设置为value，这样每次激活constant这个条件的时候，就会检查一遍相应connector的值来确保条件成立。
4. **converter(c, f)**: assembles the various connectors and constraints in the network. 首先统一创建除了输入输出所有参数的connector。之后用条件进行约束。
5. **adder(a, b, c)**: 通过`make_ternary_constraint(a, b, c, add, sub, sub, sub)`创建的约束，是一个字典
6. **multiplier(a, b, c)**: 通过`make_ternary_constraint(a, b, c, add, sub, sub, sub)`创建的约束，是一个字典

```python
def multiplier(a, b, c):
    '''The constraint that a * b = c'''
    return make_ternary_constarint(a, b, c, mul, truediv, truediv)
def adder(a, b, c):
    '''The constraint that a + b = c'''
    return make_ternary_constarint(a, b, c, add, sub, sub)
def constant(connector, value):
    '''The constraint that connector = value'''
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint
def inform_all_except(source, message, constraints):
    '''inform all constraints of the message, expect source'''
    for c in constraints:
        if c != source:
            c[message]()
def connector(name=None):
    '''A connector between constraints'''
    informant = None
    constraints = []
    
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Constradiction detected:', val, 'vs', value)
    
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    
    connector = {'val':  None,
                 'set_val':  set_value,
                 'forget':  forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)
                 }
    return connector
    
celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')

def convert(c, f):
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)
    
convert(celsius, fahrenheit)
```
```python
>>> celsius['set_val']('user', 25)
```
```bash
Celsius = 25
Fahrenheit = 77.0
```
由于convert函数在运行的时候，约束条件会存储在celsius和fahrenheit下面，因此不会被销毁。而其他的constraint会存储multiplier，因此也不会被销毁。这样就完成了一个约束系统。

# Chapter 4
## 4.2 Implicit Sequence
A sequence can be represented without each element being stored explicityly in the memory of the computer. Construct object that provides access to all of the elements of some sequential dataset without computing the value of each element in advance. Compute elements on demand.

When an element is requested from a `range`, the element is computed without conputing in advance. Only the end point of the range are stored as part of the `range` object.

### 4.2.1 Iterators
**Iterator**: an object provides sequential access to values, one by one.
two components:
* mechanism for retrieving the **next element** in the sequence
* a mechanism for **signal that the end** of the sequence has been reached and no further elements remain.

a iterator can be obtained by calling the built-in `iter` function, the contents of the iterator can be accessed by calling the built-in `next` function
```python
>>> primes = [2, 3, 5, 7]
>>> type(primes)
>>> iterator = iter(primes)
>>> type(iterator)
>>> next(iterator)
2
>>> next(iterator)
3
>>> next(iterator)
5
```

Python signals that there is no more values avaiable by raising a `StopIteration` exception when `next` is called. This expection can be handled using a `try` statement.
![alt text](image-13.png)

An iterator maintains local state to represent its position in a sequence. Each time `next` is called, that position advances. Two separate iterators can track two different positions in the same sequence. Two names for the same iterator will share a position.

Calling `iter` on an iterator will return that iterator, **not a copy**. 相当于原本iterator的别名。

### 4.2.2 Iterables
An iterable value is anything that can be passed to the built-in `iter` function.(including `strings`, `tuples`, `sets`, `dictionaries`, `iterators`)

字典也可以迭代， 顺序是键值对加入字典时的顺序。如果字典由于添加或者删除键导致其结构改变，则所有迭代器都会失效。更改键值不会更改内容的顺序或者使迭代器无效。
![alt text](image-14.png)

### Built-in Iterators
Several built-in functions take as arguments iterable values and return iterators.
`map` function: 
![alt text](image-15.png)
在使用next的时候才会call double_and_print进行计算
![alt text](image-16.png)
使用list转换的时候，只会保存return的value
`filter` function returns an iterator over, `zip` and `reversed` functions also return iterators.

### 4.2.4 For Statements
The `for` statement in Python operators on iterators. Objects are iterable if they have an `__iter__` method that returns an iterator. Iterable objects can be the value of the `<expression>` in the header of a `for` statement.
```python
for <name> in <expression>:
    <suite>
```
first evaluates the header `<expression>`. then, the `__iter__` method is invoked on that value. Until a `StopIteration` exception is raised. Python repeatedly invokes the `__next__` method on that iterator and binds the result to the `<name>` in the `for` statement. Then, it executes the `<suite>`
```python
>>> counts = [1, 2, 3]
>>> for item in counts:
        print(item)
1
2
3
```

Implement the execution rule of a `for` statement in terms of `while`, assignment, and `try` statements.
```python
items = counts.__iter__()
try:
    while True:
        item = items.__next__()
        print(item)
except StopIteration:
    pass
1
2
3
```

ps: `try` and `except`, 允许程序在遇到错误时继续运行，而不是直接崩溃
```python
try:
    risky_operation()
except SomeException as e:
    print(f'An error occurred: {e}')
```
`try`块会首先执行，如果遇到异常，会跳转到对应的`except`块执行处理逻辑
1. 捕获特定异常
```python
try:
    num = int(input("Enter a number: "))  # 用户输入非数字会引发 ValueError
except ValueError:
    print("Please enter a valid integer.")
```
2. 捕获多个异常
```python
try:
    result = 10 / int(input("Enter a number: "))  # 可能引发 ZeroDivisionError 或 ValueError
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a number.")

```
3. 捕获所有异常
```python
try:
    risky_operation()
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```
4. `else`块
如果`try`中没有发生异常，则会执行`else`中的代码
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero error!")
else:
    print(f"Result is {result}")

```
5. `finally`块
无论是否发生异常`finally`块中的代码都会执行
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    if 'file' in locals() and not file.closed:
        file.close()  # 确保文件被正确关闭
```

前后都有两个下划线的方法被称为“Magic Methods” or "Special Mehods"，通常与某些特定的功能或行为绑定。

### 4.2.5 Generators and Yield Statements
Generators allow us to define more complicated iterations.

A generator is an ***iterator*** returned by a special class of function called ***generator*** function.

Generator functions are distinguished from regular functions in that rather than containing `return` statements in their body, they use `yield` statement to return elements of a series.

Generators do not use attributes of an object to track their progress through a series. They control the execution of the generator function, which runs until the next `yield` statement is executed each time the generator's `__next__` is invoked.

```python
def letters_genetor():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current) + 1)
```
![alt text](image-17.png)
```python
>>> generator_eg = letters_genetor()
>>> generator_eg.__next__()
>>> 'a'
>>> generator_eg.__next__()
>>> 'b'
```
每次调用generator的手都会执行其对应的generator function，直到运行完第一次的yield。

The generator function would return a generator without explicitly define `__iter__` or `__next__` methods, the `yield` statement indicates that we are defining a generator function. The generator function returned by the generator function can return the yielded values.

A generator object has `__iter__` and `__next__` methods, and each call to `__next__` continues execution of the generator function from wherever it left off previously until another `yield` statement is executed.

The first time `__next__` is called, the program executes statements from the body of the `letters_generator` function until it encounters the `yield` statement. Then, it pauses and returns the value of `current.yield` statements do not destroy the newly created environment, they preserve it for later.

### 4.2.6 Iterable Interface

An object is iterable if it returns an iterator when its `__iter__` method is invoked. 

### 4.2.7 Creating Iterables with Yield

In Python, iterators only make a single pass over the elements of an underlying series. After that pass, the iterator will continue to raise a `StopIteration` exception when `__next__` is invoked.

New iterable classes can be defined by implementing the iterable interface. `LettersWithYield` class returns a new iterator over letters each time `__iter__` is invoked.
```python
class LettersWithYield:
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end
    def __iter__(self):
        next_letter = self.start
        while next_letter < self.end:
            yield next_letter
            next_letter = chr(ord(next_letter) + 1)
```

### Iterator Interface

An iterator can perform arbitary computation to either retrieve or compute next element in response to invoking `__next__`. Python signals that the end of an underlying series has been reached by rasing a `StopTeration` exception during a call to `__next__`

```python
class LetterIter:
    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end
    def __next__(self):
        if self.next_letter == self.end:
            raise StopIteration
        letter = self.next_letter
        self.next_letter = chr(ord(letter)+1)
        return letter
```

Represent infinite series by implementing a `__next__` method that neverer raises a `StopIteration` exception.
```python
class Positives:
    def __init__(self):
        self.next_positive = 1
    def __next__(self):
        result = self.next_positive
        self.next_positive += 1
        return result
```

### 4.2.10 Python Streams
**Streams** is a Lazily computed linked list. A `Stream` instance responds to requests for its `first` element and the `rest` of the stream. Like an `Link`, the `rest` of a `Stream` is itself a Stream. Unlike an `Link`, the `rest` of a stream is only computed when it is looked up, rather than being stored in advance. That is, the `rest` of a stream is computed lazily.

A stream stores a function that computes the rest of the stream. Whenever this function is called, its returned value is cached as part of the stream in an attribute called `_rest`, named with an underscore to indicate that it should not be accessed directly.

The accessible attribute `rest` is a property method that returns the rest of the stream, computing it if necessary. 
```python
class Stream:
    class empty:
        def __repr__(self):
            return 'Stream empty'
    empty = empty()
    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable'
        self.first = first
        self._compute_rest = compute_rest
    @property
    def rest(self):
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))    
```
```python
s = Stream(1, lambda: Stream(2 + 3, lambda: Stream(9)))
```
创建的时候并不会计算`2+3`只有在调用`s.rest`的时候会调用`s.compute_rest`即`lambda: Stream(2+3, lambda: Stream(9))`这时候就会计算出`2+3`的值。