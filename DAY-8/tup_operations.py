Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=()
>>> type(t)
<class 'tuple'>
>>> t = (1)
>>> t
1
>>> #this is an integer ,we need to add (,) to make single element tuple
>>> type(t)
<class 'int'>
>>> t=(1,)
>>> type
<class 'type'>
>>> type(t)
<class 'tuple'>
>>> t = (1,23.4,34+5j,'str',[1,2,3],{3,4,5},{1:1,2:3})
>>> t
(1, 23.4, (34+5j), 'str', [1, 2, 3], {3, 4, 5}, {1: 1, 2: 3})
>>> t = ( 1,2,3,4,5,1,2,3,8)
>>> t
(1, 2, 3, 4, 5, 1, 2, 3, 8)
>>> #tuple allows duplicates
>>> #tuple operations
>>> t =(1,2,3,4,5)
>>> s= (5,6,7,8,9)
>>> t+s
(1, 2, 3, 4, 5, 5, 6, 7, 8, 9)
>>> t*2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
>>> t = (1,23.4,34+5j,'str',[1,2,3],{3,4,5},{1:1,2:3},'True')
>>> t
(1, 23.4, (34+5j), 'str', [1, 2, 3], {3, 4, 5}, {1: 1, 2: 3}, 'True')
>>> t[1]
23.4
>>> t[-1]
'True'
>>> t[-3]
{3, 4, 5}
>>> t[1]
23.4
>>> t[ : ]
(1, 23.4, (34+5j), 'str', [1, 2, 3], {3, 4, 5}, {1: 1, 2: 3}, 'True')
>>> t[0:]
(1, 23.4, (34+5j), 'str', [1, 2, 3], {3, 4, 5}, {1: 1, 2: 3}, 'True')
>>> t[3:]
('str', [1, 2, 3], {3, 4, 5}, {1: 1, 2: 3}, 'True')
>>> sorted(t)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'complex' and 'float'
>>> t = (3,4,32,4,5,66,5,6,65,44,3,32,45,322)
>>> t
(3, 4, 32, 4, 5, 66, 5, 6, 65, 44, 3, 32, 45, 322)
>>> sorted(t)
[3, 3, 4, 4, 5, 5, 6, 32, 32, 44, 45, 65, 66, 322]
>>> max(t)
322
>>> min(t)
3
>>> sum(t)
636
>>> len(t)
14
>>> t.index(6)
7
>>> t.find(6)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t.find(6)
AttributeError: 'tuple' object has no attribute 'find'
>>> t.count(2)
0
>>> t.count(4)
2
>>> t = (1,2,4,[4,6,7])
>>> t
(1, 2, 4, [4, 6, 7])
>>> t[3].append(10)
>>> t
(1, 2, 4, [4, 6, 7, 10])
>>> t=()
>>> t
()
>>> any(t)
False
>>> t = (1,2,4,[4,6,7])
>>> t
(1, 2, 4, [4, 6, 7])
>>> any(t)
True
>>> all(t)
True
>>> 