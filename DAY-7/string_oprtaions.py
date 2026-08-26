Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #triming method
>>> c="           Kadali Nikhil Sai Kumar        "
>>> c
'           Kadali Nikhil Sai Kumar        '
>>> c.lstrip()
'Kadali Nikhil Sai Kumar        '
>>> c.rstrip()
'           Kadali Nikhil Sai Kumar'
>>> 
>>> a="Kadali-Nikhil-Sai-Kumar"
>>> a.split("-")
['Kadali', 'Nikhil', 'Sai', 'Kumar']
>>> a.split("-",3)
['Kadali', 'Nikhil', 'Sai', 'Kumar']
>>> a.split("-",2)
['Kadali', 'Nikhil', 'Sai-Kumar']
>>> a.rsplit("-",2)
['Kadali-Nikhil', 'Sai', 'Kumar']
>>> a='''python
java
mysql
flask
'''
>>> a.split()
['python', 'java', 'mysql', 'flask']
>>> a.splitlines()
['python', 'java', 'mysql', 'flask']
>>> " ".join(a)
'p y t h o n \n j a v a \n m y s q l \n f l a s k \n'
>>> ''.join(a)
'python\njava\nmysql\nflask\n'
>>> '@'.join(a)
'p@y@t@h@o@n@\n@j@a@v@a@\n@m@y@s@q@l@\n@f@l@a@s@k@\n'
>>> a=['python', 'java', 'mysql', 'flask']
>>> a
['python', 'java', 'mysql', 'flask']
>>> '@'.join(a)
'python@java@mysql@flask'
>>> a
['python', 'java', 'mysql', 'flask']
>>> #partitions
>>> #partition will always divide string to 3 parts
>>> s = 'java-python-c-rust'
>>> s.partition('-')
('java', '-', 'python-c-rust')
>>> s.rpartition('-')
('java-python-c', '-', 'rust')
>>> s
'java-python-c-rust'
>>> a='strings.png'
>>> a.startswith('str')
True
>>> a.startswith('hello')
False
>>> a.endswith('hello')
False
>>> a.endswith('ng')
True
>>> 'tharunkumar'.islower()
True
>>> 'BUNNY'.islower()
False
>>> 'BUNNY'.isupper()
True
>>> 'tharunkumar'.isalpha()
True
>>> 'tharunkumar1234'.isalpha()
False
>>> 'tharunkumar1234'.isalnum()
True
>>> 'tharunkumar'.isalnum()
True
>>> '12345'.isalnum()
True
>>> '12345@'.isalnum()
False
>>> '           '.isspace()
True
>>> '           12'.isspace()
False
>>> 'Tharun Kumar'.istitle()
True
>>> 'Tharun kumar'.istitle()
False
>>> 
>>> 'Tharunkumar'.isidentifier()
True
>>> '12345'.isdigit()
True
>>> "1223451".isnumeric()
True
>>> 'Tharunkumar'.isnumeric()
False
>>> '435.2345'.isdecimal()
False
>>> '432532'.isdecimal()
True