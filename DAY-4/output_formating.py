Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=15
>>> b=69.69
>>> c="tharunkumar"
>>> print(a,b,c
)
15 69.69 tharunkumar
>>> b=20.12
>>> print("a=",a "b=",b, "c=",c)
SyntaxError: invalid syntax
>>> print("a=",a ,"b=", b, "c=",c)
a= 15 b= 20.12 c= tharunkumar
>>>  print("a=",a ,"b=", b, "c=",c, sep'\n')
 
SyntaxError: unexpected indent
>>> print("a=",a ,"b=", b, "c=",c, sep'\n')
SyntaxError: invalid syntax
>>> print("a=",a ,"b=", b, "c=",c, sep='\n')
a=
15
b=
20.12
c=
tharunkumar
>>> print(f' a={a} b={b} c={c}')
 a=15 b=20.12 c=tharunkumar
>>> print("a=",a ,"b=", b, "c=",c, sep'\n')
SyntaxError: invalid syntax
>>> print('a=%d b=%f c=%s' %(a,b,c))
a=15 b=20.120000 c=tharunkumar
>>> print( 'a={} b={} c={}' .format(a,b,c))
a=15 b=20.12 c=tharunkumar
>>> print( 'a={} b={} c={}' .format(c,a,b))
a=tharunkumar b=15 c=20.12
>>> print( 'a={2} b={1} c={0}' .format(a,b,c))
a=tharunkumar b=20.12 c=15
>>> 