Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionary operations
>>> d={}
>>> type(d)
<class 'dict'>
>>> d = {1:2,3:4,5:6}
>>> d
{1: 2, 3: 4, 5: 6}
>>> del d
>>> d
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> 
>>> 
>>> #creating and adding keyvalue pairs
>>> d ={}
>>> d[1]=1
>>> d
{1: 1}
>>> d[2,3]=3
>>> d
{1: 1, (2, 3): 3}
>>> d['str']=3
>>> d
{1: 1, (2, 3): 3, 'str': 3}
>>> d[(1,2,3,4)]=4
>>> d
{1: 1, (2, 3): 3, 'str': 3, (1, 2, 3, 4): 4}
>>> d[3+4j]=5
>>> d
{1: 1, (2, 3): 3, 'str': 3, (1, 2, 3, 4): 4, (3+4j): 5}
>>> d[True]=7
>>> d
{1: 7, (2, 3): 3, 'str': 3, (1, 2, 3, 4): 4, (3+4j): 5}
>>> 
>>> 
>>> d
{1: 7, (2, 3): 3, 'str': 3, (1, 2, 3, 4): 4, (3+4j): 5}
>>> dict={}
>>> del dict
>>> d
{1: 7, (2, 3): 3, 'str': 3, (1, 2, 3, 4): 4, (3+4j): 5}
>>> t = {}
>>> t[1]= 23
>>> t
{1: 23}
>>> del t
>>> t
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> 
>>> 
>>> # Different types of values can be stored in a dictionary
>>> t = {}
>>> t[1]= 23
>>> d[34] = 'str'
>>> t[34] = 'str'
>>> t
{1: 23, 34: 'str'}
>>> t[45] = 12+4j
>>> t[12]=(1,12,23,4)
>>> t[13]=33.24
>>> t[41]=False
>>> t[23]=[3,4,5,6]
>>> t[15] = {2:3,4:5,6:7}
>>> t
{1: 23, 34: 'str', 45: (12+4j), 12: (1, 12, 23, 4), 13: 33.24, 41: False, 23: [3, 4, 5, 6], 15: {2: 3, 4: 5, 6: 7}}
>>> {1: 23, 34: 'str', 45: (12+4j), 12: (1, 12, 23, 4), 13: 33.24, 41: False, 23: [3, 4, 5, 6], 15: {2: 3, 4: 5, 6: 7}}
{1: 23, 34: 'str', 45: (12+4j), 12: (1, 12, 23, 4), 13: 33.24, 41: False, 23: [3, 4, 5, 6], 15: {2: 3, 4: 5, 6: 7}}
>>> # Lists, sets and dictionaries cannot be used as dictionary keys.
>>> # Dictionary values can contain any data type.
SyntaxError: invalid syntax
>>> 
>>> 
>>> t
{1: 23, 34: 'str', 45: (12+4j), 12: (1, 12, 23, 4), 13: 33.24, 41: False, 23: [3, 4, 5, 6], 15: {2: 3, 4: 5, 6: 7}}
>>> d[22]=None
>>> d
{1: 7, (2, 3): 3, 'str': 3, (1, 2, 3, 4): 4, (3+4j): 5, 34: 'str', 22: None}
>>> # Accessing values using keys
>>> data ={'name':'tharun','batch':65,'course':'PFS'}
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS'}
>>> data['name']
'tharun'
>>> data['tharun']
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    data['tharun']
KeyError: 'tharun'
\
>>>  # Membership operator checks keys
 
>>> 
>>> 'tharun' in data
False
>>> 'name' in data
True
>>> 'batch'in data
True
>>> 'PFS' in data
False
>>> #get()
>>> data.get('name)
	 
SyntaxError: EOL while scanning string literal
>>> data.get('name')
'tharun'
>>> data.get('tharun')
>>> data.get('course')
'PFS'
>>>  # Adding a new key-value pair
 
>>> data['phno']= 1234567890
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'phno': 1234567890}
>>> #update()
>>> #update is used to add multiple values
>>> data.update({'email':'tharun123@gmail.com','py':2026})
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'phno': 1234567890, 'email': 'tharun123@gmail.com', 'py': 2026}
>>>  # clear()
 
>>> d.clear()
>>> d
{}
>>> # Dictionary keys cannot be modified directly.
>>> # A key must be deleted and a new key must be added.
>>> 
>>> 
>>> #pop()
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'phno': 1234567890, 'email': 'tharun123@gmail.com', 'py': 2026}
>>> data.pop('email')
'tharun123@gmail.com'
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'phno': 1234567890, 'py': 2026}
>>> data.pop('phno')
1234567890
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'py': 2026}
>>> len(data)
4
>>> 
>>> #keys(),values() and items()
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'py': 2026}
>>> data.keys()
dict_keys(['name', 'batch', 'course', 'py'])
>>> data.values()
dict_values(['tharun', 65, 'PFS', 2026])
>>> data.items()
dict_items([('name', 'tharun'), ('batch', 65), ('course', 'PFS'), ('py', 2026)])
>>> 
>>> #sorted(),min(),and max()
>>> sorted(data)
['batch', 'course', 'name', 'py']
>>> max(data)
'py'
>>> min(data)
'batch'
>>>  # Assignment and copy()
 
>>> d = {1: 1, 2: 4, 5: 5}
>>> d
{1: 1, 2: 4, 5: 5}
>>> m = d
>>> m[4] = 4
>>> m
{1: 1, 2: 4, 5: 5, 4: 4}
>>> d
{1: 1, 2: 4, 5: 5, 4: 4}
>>> # copy() creates a separate dictionary
>>> n = d.copy()
>>> n[5] = 8778
>>> n
{1: 1, 2: 4, 5: 8778, 4: 4}
>>> d
{1: 1, 2: 4, 5: 5, 4: 4}
>>> 
>>> 
>>>  # setdefault()
 
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'py': 2026}
>>> data.get('name)
	 
SyntaxError: EOL while scanning string literal
>>> data.get('name')
'tharun'
>>> data.setdefult('batch','java')
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    data.setdefult('batch','java')
AttributeError: 'dict' object has no attribute 'setdefult'
>>> data.setdefault('gender', 'male')
'male'
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'py': 2026, 'gender': 'male'}
>>> data.setdefault('batch','java')
65
>>> data
{'name': 'tharun', 'batch': 65, 'course': 'PFS', 'py': 2026, 'gender': 'male'}
>>>  # fromkeys()
 
>>> dict.fromkeys(["python", "java", "mysql"], 33)
{'python': 33, 'java': 33, 'mysql': 33}
>>> 