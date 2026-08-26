Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string operations
>>> #concatenation
>>> #repataion
>>> a="Tharun"
>>> b=" Kumar"
>>> a+b
'Tharun Kumar'
>>> a*10
'TharunTharunTharunTharunTharunTharunTharunTharunTharunTharun'
>>> #concatenation
>>> a="Tharun"
>>> b=" Kumar"
>>> a+b
'Tharun Kumar'
>>> #repataion
>>> a*10
'TharunTharunTharunTharunTharunTharunTharunTharunTharunTharun'
>>> #indexing
>>> a
'Tharun'
>>> a[0]
'T'
>>> a[5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[5]
'n'
>>> a[:4]
'Thar'
>>> c=a+b
>>> c
'Tharun Kumar'
>>> c[:14]
'Tharun Kumar'
>>> c[6:14]
' Kumar'
>>> c[7:14]
'Kumar'
>>> #slicing
>>> c[:14]
'Tharun Kumar'
>>> 
>>> c[7:14]
'Kumar'
>>> #membership
>>> "T" in c
True
>>> "K" in c
True
>>> "b" in c
False
>>> "b" in c
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> c[:-12]
''
>>> c[-1:]
'r'
>>> c[-1:-12]
''
>>> c[-1:-5]
''
>>> c[-5:]
'Kumar'
>>> c[-12:]
'Tharun Kumar'
>>> c[-12:-4]
'Tharun K'
>>> #string menthods
>>> len(c)
12
>>> ord("a")
97
>>> chr(10)
'\n'
>>> sorted(c)
[' ', 'K', 'T', 'a', 'a', 'h', 'm', 'n', 'r', 'r', 'u', 'u']
>>> max(c)
'u'
>>> min(c)
' '
>>>  c.upper()
 
SyntaxError: unexpected indent
>>> c.upper()
'THARUN KUMAR'
>>> c.lower()
'tharun kumar'
>>> c.capitalize()
'Tharun kumar'
>>> c.title()
'Tharun Kumar'
>>> c.caseflod()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    c.caseflod()
AttributeError: 'str' object has no attribute 'caseflod'
>>> c.swapcase()
'tHARUN kUMAR'
>>> c.center
<built-in method center of str object at 0x0000013A21CF7BF0>
>>> 
>>> c.center(20,"-")
'----Tharun Kumar----'
>>> c.ljust(20."-")
SyntaxError: invalid syntax
>>> c=ljust(20,"-")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    c=ljust(20,"-")
NameError: name 'ljust' is not defined
>>> c.ljust(20,"-")
'Tharun Kumar--------'
>>> c.rjust(20,"-")
'--------Tharun Kumar'
>>> "8096"zfill(7)
SyntaxError: invalid syntax
>>> "8096".zfill(7)
'0008096'
>>> "8096".zfill(6)
'008096'
>>> "96".zfill(6)
'000096'
>>> c
'Tharun Kumar'
>>> c.find("run")
3
>>> c.fid("Tharun")
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    c.fid("Tharun")
AttributeError: 'str' object has no attribute 'fid'
>>> c.find("Tharun")
0
>>> c.find("a")
2
>>> c.rfind("a)
	
SyntaxError: EOL while scanning string literal
>>> c.rfind("a")
10
>>> c.find("s")
-1
>>> c.index("a")
2
>>> c.index("k")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    c.index("k")
ValueError: substring not found
>>>  c.index("K")
 
SyntaxError: unexpected indent
>>> c.index("K")
7
>>> c.count("a")
2
>>> c.count("K")
1
>>> c.count("r")
2
>>> c
'Tharun Kumar'
>>> c.replace("a","1")
'Th1run Kum1r'
>>> c
'Tharun Kumar'
>>> c.replace("r","4")
'Tha4un Kuma4'
>>> # Difference between index() and find()
>>> # index() raises ValueError when the substring is not found.
>>> # find() returns -1 when the substring is not found.

>>> # maketrans() and translate()
>>> s = 'thor is powerful character in avengers'
>>> s.maketrans('thor', 'hulk')
{116: 104, 104: 117, 111: 108, 114: 107}
>>> s.translate(s.maketrans('thor', 'hulk'))
'hulk is plwekful cuakachek in avengeks'

>>> c.maketrans("aeiou","#@&$%")
{97: 35, 101: 64, 105: 38, 111: 36, 117: 37}

>>> c.translate({97: 35, 101: 64, 105: 38, 111: 36, 117: 37})
'Th#r%n K%m#r'

>>> # Encoding
>>> text = 'hello'
>>> text.encode()
b'hello'
>>> text.encode('utf-8')
b'hello'

>>> # Decoding
>>> b'hello'.decode()
'hello'
>>> b'hello'.decode('utf-8')
'hello'
