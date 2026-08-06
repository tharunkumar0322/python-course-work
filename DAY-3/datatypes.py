Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #data types
>>> #int
>>> a=10
>>> type (a)
<class 'int'>
>>> #float
>>> b=12.1
>>> type(b)
<class 'float'>
>>> #complex
>>> b=8+5j
>>> type(b)
<class 'complex'>
>>> #string
>>> s='xyz'
>>> type(s)
<class 'str'>
>>> #lisr
>>> #list
>>> l=[1,2,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> l
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> l=[1,2,3,4]
>>> type(l)
<class 'list'>
>>> #tuple
>>> id(l)
2663027763840
>>> l.append(12)
>>> l
[1, 2, 3, 4, 12]
>>> t=(9,8,7,6)
>>> t
(9, 8, 7, 6)
>>> id(t)
2663059687040
>>> t.index
<built-in method index of tuple object at 0x0000026C0ABA0680>
>>> 