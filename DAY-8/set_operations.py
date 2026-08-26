Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #set
>>> s = {}
>>> type(s)
<class 'dict'>
>>> s = set()
>>> type(s)
<class 'set'>
>>> s = {345,12345,6547,23,567,342,65487,234,323}
>>> s
{323, 567, 234, 65487, 6547, 342, 23, 345, 12345}
>>> s = {1,1,1,1,1,1,1}
>>> s
{1}
>>> s = {345,12345,6547,23,567,342,65487,234,323}
>>> s
{323, 567, 234, 65487, 6547, 342, 23, 345, 12345}
>>> s.add(1)
>>> s
{1, 323, 567, 234, 65487, 6547, 342, 23, 345, 12345}
>>> s.add(12.12)
>>> s
{1, 323, 567, 234, 12.12, 65487, 6547, 342, 23, 345, 12345}
>>> s.add(23+3j)
>>> s
{(23+3j), 1, 323, 567, 234, 12.12, 65487, 6547, 342, 23, 345, 12345}
>>> s.add('str')
>>> s
{(23+3j), 1, 323, 567, 234, 12.12, 65487, 6547, 342, 23, 345, 'str', 12345}
>>> s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: unhashable type: 'list'
>>> s.add((3,45,6))
>>> s
{(23+3j), 1, 323, 567, 234, 12.12, (3, 45, 6), 65487, 6547, 342, 23, 345, 'str', 12345}
>>> s.add({1:1,2:1})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.add({1:1,2:1})
TypeError: unhashable type: 'dict'
>>> s.add(False)
>>> s
{(23+3j), 1, False, 323, 567, 234, 12.12, (3, 45, 6), 65487, 6547, 342, 23, 345, 'str', 12345}
>>> #list, set, dict are not allowed inside set
>>>  #set operations
>>> s = {1,2,3,4,5}
>>> t = {6,7,8,9}
>>> s+t
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s+t
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s*2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> s
{1, 2, 3, 4, 5}
>>> t
{8, 9, 6, 7}
>>> 12 in s
False
>>> 9 in t
True
>>> t = {1,3,4,9,5}
>>> t
{1, 3, 4, 5, 9}
>>> t&s
{1, 3, 4, 5}
>>> t|s
{1, 2, 3, 4, 5, 9}
>>> t-s
{9}
>>> s-t
{2}
>>> s<=t
False
>>> s>=t
False
>>> #indexing and slicing not supported by set
>>> t[1]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t[1]
TypeError: 'set' object is not subscriptable
>>> t.index(1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    t.index(1)
AttributeError: 'set' object has no attribute 'index'
>>> all(t)
True
>>> any(t)
True
>>> sum(t)
22
>>> min(t)
1
>>> max(t)
9
>>> len(t)
5
>>> sorted(t)
[1, 3, 4, 5, 9]
>>> r = t.copy()
>>> r
{1, 3, 4, 5, 9}
>>> t.add(11)
>>> t
{1, 3, 4, 5, 9, 11}
>>> r
{1, 3, 4, 5, 9}
>>> #add is for adding single element
>>> s
{1, 2, 3, 4, 5}
>>> s.add(12)
>>> s
{1, 2, 3, 4, 5, 12}
>>> s.update(13,14,15)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.update(13,14,15)
TypeError: 'int' object is not iterable
>>> s.update({13,14,15})
>>> s
{1, 2, 3, 4, 5, 12, 13, 14, 15}
>>> #update is for add multiple elements
>>> s.pop()
1
>>> s.remove(5)
>>> s
{2, 3, 4, 12, 13, 14, 15}
>>> s.discord(123)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.discord(123)
AttributeError: 'set' object has no attribute 'discord'
>>> s
{2, 3, 4, 12, 13, 14, 15}
>>> s.discard(123)
>>> s
{2, 3, 4, 12, 13, 14, 15}
>>> #discard wont throw any error if value does not exist
>>> s.clear()
>>> s
set()
>>> 