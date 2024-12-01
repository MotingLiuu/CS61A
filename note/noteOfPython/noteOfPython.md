# 常用工具
## in
in 可以查询一个字符串是否在另一个字符串中（作为另一个字符串的连续子串出现）。
## str.split()
`str.split()`根据空格将字符分隔为单词列表

## 正则表达式
* 字符：匹配自身`a`匹配字母"a"
* 字符类：匹配某类字符的集合。`[abc]`匹配`a`，`b`，`c`。
* 量词：指定字符类或字符的出现次数`a*`匹配零个或者多个`a`
* 位置符号：匹配文本中的特定位置，`^`匹配行的开头。`$`匹配行的结尾
* 分组：通过`()`将多个字符组合在一起`(abc)_+`匹配一个躲着多个"abc"

常用模式
1. 字符匹配
* 单个字符：`a`匹配"a"
* 字符类：`[abc]`匹配`a`，`b`,`c`。可以使用`^`匹配不是"a","b","c"的字符
* 预定义字符类：
    * `\d`匹配数字，等同于[0-9]
    * `\w`匹配字母，数字，下划线，等同于[a-zA-Z0-9_]
    *`\s`匹配任意空白字符，如空格，制表符

2. 量词
* `*`匹配零个或多个前面的元素，`a*`匹配空字符串'a','aa'
* `+`同上
* `?`匹配零个或一个前面的元素`a?`匹配空字符串或'a'
* `{m}`匹配恰好n个前面的元素，例如`a{3}`匹配'aaa'
* `{n,}`匹配至少n个前面的元素，`a{2,}`匹配'aa','aaa','aaaa'
* `{n,m}`匹配n到m个前面的元素例如`a{2,4}`匹配'aa','aaa','aaaa'

3. 位置符号
* `^`匹配字符串的开头，`^Hello`匹配以'Hello'开头的字符串
* `$`匹配字符串的结尾，`world$`匹配以`world`结尾的字符串
* `\b`匹配单词边界，`\bword\b`匹配`word`但不匹配`sword`单词边界位于一个单词字符和一个非单词字符之间，并且可以出现在单词的开头和单词的结尾。`\b\w+\b`：匹配从单词边界开始，包含至少一个单词字符（`\w+`），并在单词边界结束的完整单词。

4.分组和捕获
* 分组 用圆括号`()`将多个字符组合在一起`(abc)+`匹配一个或多个`abc`
* 捕获 正砸表达式中的括号可以捕获匹配的子串，`(\d)-(\d+)`能捕获两个数字，分别对应两个捕获组。

5. 断言（Assertions）
* 先行断言：检查某个模式是否在当前位置之后`a(?=b)`匹配`a`之后在其后跟着`b`的时候
* 先行断言否定：检查某个模式是否不在当前位置之后`a(?!b)`匹配`a`只有在其后没有`b`的时候
* 后行断言：检查某个模式是否在当前位置之前`(?<=b)a`匹配'a'只有在其前面是'b'的时候
* 后行否定断言：检查某个模式是否不在当前的位置之前，例如，`(?<!b)a`匹配'a'只有在其前面不是'b'的时候

6. 贪婪与非贪婪匹配
* 贪婪匹配：默认情况下正则表达式贪婪，尽可能多地匹配
* 非贪婪匹配：使用`?`

## random
### random.randint(a, b)
生成一个指定范围内[a, b]的int
```python
import random

random_number = random.randint(1, 10)
print(random_number)
```
### random.randint(low, high, size)
生成多个随机整数[low, high)
```python
random_number = np.random.randint(1, 10, size=5)
print(random_numbers)
```
### random.sample(range(start, stop), k)
生成多个指定范围内[start, stop)不重复的int
```python
random_numbers = random.sample(range(1, 10), 3)
print(random_numbers)
```


# 数据类型

## List
### map
`map(function, iterable)`
`function`要应用的函数
`iterable`一个或者多个可迭代对象
返回值为一个`map`对象（迭代器）


```python
nums=[1, 2, 3, 4]
squared = map(lambda x: x**2, nums)
print(list(squared))

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
summed = map(lambda x, y: x + y, nums1, nums2)
print(list(summed))  # 输出: [5, 7, 9]

# 示例：获取字典中每个键的值
encode_dict = {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'b', 'c']
values = map(encode_dict.get, keys)
print(list(values))  # 输出: [1, 2, 3]
```

## Dictionaries
```python
>>> d = {2: 4, 'two': ['four'], (1, 1): 4}
>>> d[2]
4
>>> d['two']
['four']
>>> d[(1, 1)]
4
```
The sequence of keys or values or key-value pairs can be accessed `.keys()` or `.values()` or `.items()`
```python
>>> for k in d.keys():
...     print(k)
...
2
two
(1, 1)
>>> for v in d.values():
...     print(v)
...
4
['four']
4
>>> for k, v in d.items():
...     print(k, v)
...
2 4
two ['four']
(1, 1) 4
```
whether a dictionary contains a key using `in`:
```python
>>> 'two' in d
True
>>> 4 in d
False
```
also there is dictionary comprehensive
```python
>>> {3*x: 3*x + 1 for x in range(2, 5)}
{6: 7, 9: 10, 12: 13}
```

### dict.get(key, default=None)
如果key存在返回对应值，不存在返回`default`
```python
# 示例
encode_dict = {'a': 1, 'b': 2, 'c': 3}

# 获取键 'a' 的值
print(encode_dict.get('a'))  # 输出: 1

# 获取不存在的键 'd'
print(encode_dict.get('d'))  # 输出: None

# 设置默认值
print(encode_dict.get('d', -1))  # 输出: -1

# 定义字典和序列
encode_dict = {'a': 1, 'b': 2, 'c': 3}
sequence = ['a', 'b', 'd', 'c']

# 使用 map 和 get，处理未知键
encoded_sequence = list(map(lambda x: encode_dict.get(x, -1), sequence))
print(encoded_sequence)  # 输出: [1, 2, -1, 3]
```

# 文件处理相关
## Open
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
1. `file`
文件路径，相对路径或绝对路径，路径不正确会有`FileNotFoundError`
2. `mode`
文件打开模式
`r`只读
`w`写入，如果文件存在，会清空内容；否则创建文件
`x`独占创建方式打开。若文件已经存在，会引发`FileExistsError`
`a`以追加模式打开。如果文件已经存在，写入内容会附加到末尾
`b`以二进制模式打开（可以与其他模式组合`rb`)
`t`以文本模式打开
`+`以读写模式打开（可以与其他模式组合如`r+`)
3. `buffering`
* 缓冲设置
    * `-1`根据文件类型使用系统默认缓冲
    * `0`无缓冲（仅适用于二进制模式）
    * 正整数，指定缓冲区大小，以字节为单位
4. `encoding`
* 字符编码方式
    * `utf-8`（默认值）
    * `ignore`忽略错误
    * `replace`用替代字符（通产是`?`）替换错误字符
5. `errors`
* 定义编码/解码错误的处理方式：
    `strict`：引发错误（默认值）。
    `ignore`：忽略错误。
    `replace`：用替代字符（通常是 ?）替换错误字符。
6. `newline`:
控制换行符的处理，仅适用于文本模式。
`None`（默认值）：自动换行符处理。
`''`：不转换换行符。
7. `closefd`:
仅适用于文件描述符（非文件路径）。
如果为`False`，`close()`方法不会关闭底层文件描述符。
8. `opener`:
自定义打开文件的处理方式（高级用法）。

Return Value
`open()`返回一个文件对象
1. `read()`读取文件内容
2. `write()`写入文件内容
3. `close()`关闭文件
4. `seek()`移动文件指针·
5. `tell()`返回文件指针位置

全部读取
```python
with open('eg.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
```
按行读取
```python
with open('eg.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
```
读取为列表
```python
with open('eg.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)
```
覆盖写入
```python
with open('eg.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.')
```
追加写入
```python
with open('eg.txt', 'a', encoding='utf-8') as file:
    file.write('/nAppending new content.')
```
二进制读取
```python
with open('eg.jpg', 'rb') as file:
    data = file.read()
    print(data[:10])
```
二进制写入
```python
with open('eg.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03')
```
