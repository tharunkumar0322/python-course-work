Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #data_types
>>> #int
>>> 
>>> a=10
>>> type(a)
<class 'int'>
>>> #float
>>> b=123.445
>>> type(b)
<class 'float'>
>>> #complex
>>> c=4+5j
>>> type(c)
<class 'complex'>
>>> #string
>>> name='Tharunkumar'
>>> name
'Tharunkumar'
>>> type(name)
<class 'str'>
>>> #list
>>> l=[1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> id(l)
2664170789760
>>> l.append(5)
>>> l
[1, 2, 3, 4, 5]
>>> id(l)
2664170789760
>>> type(l)
<class 'list'>
>>> #tuple
>>> t=(1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> #set
>>> s={1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> s.append(6)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.append(6)
AttributeError: 'set' object has no attribute 'append'
>>> s.add(6)
>>> s
{1, 2, 3, 4, 5, 6}
>>> type(s)
<class 'set'>
>>> #dict
>>> d={'a':1,'b':2,'c':3}
>>> type(d)
<class 'dict'>
>>> #boolean
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
>>> #none
>>> v=None
>>> type(v)
<class 'NoneType'>
>>> v
>>> 