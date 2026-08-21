Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> #int to others
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> #float to others
>>> b = 123.45
>>> type(b)
<class 'float'>
>>> int(b)
123
>>> complex(b)
(123.45+0j)
>>> str(b)
'123.45'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
>>> bool(b)
True
>>> #complex to others
>>> c=5+6j
>>> type(c)
<class 'complex'>
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> str(c)
'(5+6j)'
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
>>> bool(c)
True
>>> #string to others
>>> d='tharun'
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'tharun'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float(d)
ValueError: could not convert string to float: 'tharun'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complex(d)
ValueError: complex() arg is a malformed string
>>> list(d)
['t', 'h', 'a', 'r', 'u', 'n']
>>> tuple(d)
('t', 'h', 'a', 'r', 'u', 'n')
>>> set(d)
{'t', 'n', 'u', 'h', 'a', 'r'}
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(d)
True
>>> #list to otthers
>>> l = [1,2,3,4]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a number, not 'list'
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> str(l)
'[1, 2, 3, 4]'
>>> tuple(l)
(1, 2, 3, 4)
>>> set(l)
{1, 2, 3, 4}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> #tuple to others
>>> t = (1,2,3,4)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a number, not 'tuple'
>>> str(t)
'(1, 2, 3, 4)'
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> list(t)
[1, 2, 3, 4]
>>> set(t)
{1, 2, 3, 4}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> #set to others
>>> s = {1,2,3,4,5}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a number, not 'set'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> str(s)
'{1, 2, 3, 4, 5}'
>>> list(s)
[1, 2, 3, 4, 5]
>>> tuple(s)
(1, 2, 3, 4, 5)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> m = {'a':1,'b':2,'c':3,'d':4}
>>> m
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> int(m)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    int(m)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> float(m)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    float(m)
TypeError: float() argument must be a string or a number, not 'dict'
>>> complex(m)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    complex(m)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(m)
"{'a': 1, 'b': 2, 'c': 3, 'd': 4}"
>>> list(m)
['a', 'b', 'c', 'd']
>>> tuple(m)
('a', 'b', 'c', 'd')
>>> set(m)
{'a', 'c', 'd', 'b'}
>>> bool(m)
True
>>> True
True
>>> 
>>> #boolean to others
>>> f = True
>>> int(f)
1
>>> float(f)
1.0
>>> complex(f)
(1+0j)
>>> str(f)
'True'
>>> list(f)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    list(f)
TypeError: 'bool' object is not iterable
>>> tuple(f)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    tuple(f)
TypeError: 'bool' object is not iterable
>>> set(f)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    set(f)
TypeError: 'bool' object is not iterable
>>> dict(f)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    dict(f)
TypeError: 'bool' object is not iterable
>>> 