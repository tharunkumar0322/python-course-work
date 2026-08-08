Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Input formating
>>> # int float complex str list tuple set bool
>>> a= input()

>>> a
''
>>> a= input()
Tharun
>>> a
'Tharun'
>>> b=int(input("Enter age:"))
Enter age:21
>>> c=float("Enter cgpa:"))
SyntaxError: unmatched ')'
>>> c=float(input("Enter cgpa:"))
Enter cgpa:6.9
>>> c
6.9
>>> print(c)
6.9
>>> names=input()
Tharun Bunny Prasad
>>> names
'Tharun Bunny Prasad'
>>> names.split()
['Tharun', 'Bunny', 'Prasad']
>>> names="Tharun,Bunny,Prasad"
>>> names.split(,)
SyntaxError: invalid syntax
>>> names.split(",")
['Tharun', 'Bunny', 'Prasad']
>>> names=tuple("Tharun,Bunny,Prasad")
>>> names
('T', 'h', 'a', 'r', 'u', 'n', ',', 'B', 'u', 'n', 'n', 'y', ',', 'P', 'r', 'a', 's', 'a', 'd')
>>> 
>>> names.split(",")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    names.split(",")
AttributeError: 'tuple' object has no attribute 'split'
>>> tuple(names.split(","))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(names.split(","))
AttributeError: 'tuple' object has no attribute 'split'
>>> names=tuple(input("Tharun,Bunny,Prasad").split(","))
Tharun,Bunny,Prasad
>>> names
('',)
>>> names=tuple(input("Enter names:").split(","))
Enter names:Tharun,Bunny,Prasad
>>> names
('Tharun', 'Bunny', 'Prasad')
>>> names=set(input().split())
Tharun,Bunny,Prasad
>>> names
{'Tharun,Bunny,Prasad'}
>>>  marks = input().split()
 
SyntaxError: unexpected indent
>>> marks = input().split()
12 15 16 17 18
>>> marks
['12', '15', '16', '17', '18']
>>> map(int(marks))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    map(int(marks))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> map(int,marks)
<map object at 0x000001D61855E0D0>
>>> list(map(int,marks))
[12, 15, 16, 17, 18]
>>> marks=list(map(int,input("Enter marks:").split()))
Enter marks:69 75 79 25
>>> marks
[69, 75, 79, 25]
>>> marks=tuple(map(int,input("Enter marks:").split()))
Enter marks:69 75 79 25
>>> marks
(69, 75, 79, 25)
>>> marks=set(map(int,input("Enter marks:").split()))
Enter marks:69 75 79 25
>>> marks
{25, 75, 69, 79}
>>> prices=list(map(float,input("Enter marks:").split()))
Enter marks:
>>> prices=list(map(float,input("Enter prices:").split()))
Enter prices:65.44 24.22 47.69 
>>> prices
[65.44, 24.22, 47.69]
>>> prices=tuple(map(float,input("Enter prices:").split()))
Enter prices:65.44 24.22 47.69 
>>> prices
(65.44, 24.22, 47.69)
>>> prices=set(map(float,input("Enter prices:").split()))
Enter prices:65.44 24.22 47.69 
>>> prices
{24.22, 65.44, 47.69}
>>> a,b=[1,2]
>>> a
1
>>> b
2
>>> a,b,c=[10.59.69 "str"]
SyntaxError: invalid syntax
>>> a,b,c=[10 59.69 "str"]
SyntaxError: invalid syntax
>>> a,b,c=[10,59.69,"str"]
>>> a
10
>>> b
59.69
>>> c
'str'
>>> email,password= input("Enter mail and password").split()
Enter mail and password xyz@gmail.com 12345
>>> email
'xyz@gmail.com'
>>> passwaord
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    passwaord
NameError: name 'passwaord' is not defined
>>> password
'12345'
>>> name,marks = input("Enter the name and marks ").split()
Enter the name and marks Nikhil 00
>>> name
'Nikhil'
>>> marks
'00'
>>> int(marks)
0
>>> a,b,c =list(map(int,input().split()))
25 35 45
\
>>> a
25
>>> b
35
>>> c
45
>>> status= eval(input())

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    status= eval(input())
  File "<string>", line 0
    
SyntaxError: unexpected EOF while parsing
>>> status = eval(input())
True
>>> status
True
>>> type(status)
<class 'bool'>
>>> status= eval(input())
2+3j
>>> status
(2+3j)
>>> type(status)
<class 'complex'>
>>> tatus= eval(input())
[1,2,3,4]
>>> type(status)
<class 'complex'>
>>> status= eval(input())
[1,2,3,4]
>>> type(status)
<class 'list'>
>>> status= eval(input())
{1,2,3,4,5}
>>> type(status)
<class 'set'>
>>> status= eval(input())
(1,2,3,4,5)
>>> type(status)
<class 'tuple'>
>>> status= eval(input())
{1:2,3:4,5:6}
>>>  type(status)
 
SyntaxError: unexpected indent
>>>  type(status)
 
SyntaxError: unexpected indent
>>> type(status)
<class 'dict'>
>>> status
{1: 2, 3: 4, 5: 6}
>>> status= eval(input())
[1,2,3,4]
>>> status
[1, 2, 3, 4]
>>> 