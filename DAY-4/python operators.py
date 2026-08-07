Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python operators
>>> #arithematic operator
>>> a=10
>>> b=20
>>> a+b
30
>>> a-b
-10
>>> a*b
200
>>> b/3
6.666666666666667
>>> b//2
10
>>> b%2
0
>>> #comparison operator
>>> a=10
>>> b=5
>>> a>b
True
>>> a<b
False
>>> a<=b
False
>>> a>=b
True
>>> a=!b
SyntaxError: invalid syntax
>>> a!=b
True
>>> a==b
False
>>> #assignment operator
>>> a=15
>>> a=a+10
>>> a
25
>>> a+=5
>>> a
30
>>> a-=17
>>> a
13
>>> a*=2
>>> a
26
>>> a/=2
>>> a
13.0
>>> 
>>> a//=2
>>> a
6.0
>>> a%2
0.0
>>> #Relational operator
>>> email = true
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    email = true
NameError: name 'true' is not defined
>>> email = True
>>> password = False
>>> email and passwaord
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    email and passwaord
NameError: name 'passwaord' is not defined
>>> email and password
False
>>> 6%==2 and 9%==3
SyntaxError: invalid syntax
>>> 6%=2 and 9%=3
SyntaxError: 'literal' is an illegal expression for augmented assignment
>>> 
>>> 6%==0 and 9%==0
SyntaxError: invalid syntax
>>> 7%2==0 and 9%3==0
False
>>> 7%2==0 or 9%3==0
True
>>> #membership operator
>>> #only string list tuple set dict
>>> #string
>>> name = 'codegnan'
>>> n in name
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    n in name
NameError: name 'n' is not defined
>>> 'n' in name
True
>>> list=[1,2,3,4]
>>> 4 in l
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    4 in l
NameError: name 'l' is not defined
>>> 4 in list
True
>>> 6 in list
False
>>> 6 in list
False
>>> 7 not in list
True
>>> tuple(1,2,3,4,50
)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tuple(1,2,3,4,50
TypeError: tuple expected at most 1 argument, got 5
>>> tuple=(1,2,3,4,500
)
>>> 10 in tuple
False
>>> 500 in tuple
True
>>> 20 in tuple
False
>>> 35 not in tuple
True
>>> set={1,3,5,7}
>>> 3 in set
True
>>> 2 in set
False
>>> dict= {"name" : "tharun ", "batch":45, "course":pfs}
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dict= {"name" : "tharun ", "batch":45, "course":pfs}
NameError: name 'pfs' is not defined
>>>  dict= {"name" : "tharun ", "batch":45, "course":"pfs"}
 
SyntaxError: unexpected indent
>>> dict= {"name" : "tharun ", "batch":45, "course":"pfs"}
>>> name in dict
False
>>> tharun in dict
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    tharun in dict
NameError: name 'tharun' is not defined
>>> "tharun" in dict
False
>>> l=[1,2,3,4]
>>> m=[1,2,34]
>>> id(l)
1759917821440
>>> id(m)
1759917883136
>>> l==m
False
>>> l is m
False
>>> n==m
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    n==m
NameError: name 'n' is not defined
>>> n = m
>>> n
[1, 2, 34]
>>> id(n)
1759917883136
>>> n is m
True
>>> l is m
False
>>> #bitwise operator
>>> # & | ^  ~ << >>
>>> 12 & 13
12
>>> 11 & 13
9
>>> 11 | 13
15
>>> 12 | 13
13
>>> 12^13
1
>>> ~12
-13
>>> 