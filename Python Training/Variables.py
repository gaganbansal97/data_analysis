Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> a
5
>>> print (a)
5
>>> type(a)
<class 'int'>
>>> y = 2.5
>>> type(y)
<class 'float'>
>>> #string
>>> a='hello'
>>> a
'hello'
>>> type(a)
<class 'str'>
>>> b='2'
>>> type(b)
<class 'str'>
>>> q1 = True
>>> q1
True
>>> type(q1)
<class 'bool'>
>>> A = 10
>>> B= 5
>>> C = A + B
>>> C
15
>>> D = B / A
>>> D
0.5
>>> ---
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import math
>>> math.sqrt(A)
3.1622776601683795
>>> math.sqrt(144)
12.0
>>> round(math.sqrt(A))
3
>>> greeting = "Hello"
>>> name = "Gagan"
>>> message = greeting + " " + name
>>> print(message)
Hello Gagan
>>> greeting+name
'HelloGagan'
>>> E = 2.5
>>> A+E
12.5
>>> type(A+E)
<class 'float'>
>>> A/B
2.0
>>> A/0
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    A/0
ZeroDivisionError: division by zero
>>> 0/A
0.0
>>> A*E
25.0
>>> A-E
7.5
>>> greeting - name
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    greeting - name
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> name[:3]
'Gag'
>>> name[1:3]
'ag'
>>> #True
>>> #False
>>> 4 < 5
True
>>> 10 > 23
False
>>> 4==5
False
>>> 4!=5
True
>>> 4<>5
SyntaxError: invalid syntax
>>> 4 <> 5
SyntaxError: invalid syntax
>>> type(4<5)
<class 'bool'>
>>> not(5 > 1)
False

>>> not(5>1)
False
>>> a
'hello'
>>> 
a
'hello'
>>> while()
{
	
SyntaxError: invalid syntax
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
5
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Loop.py", line 4, in <module>
    print ('Value of A is ' + a)
TypeError: Can't convert 'int' object to str implicitly
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Loop.py", line 4, in <module>
    print ('Value of A is ' + int(a))
TypeError: Can't convert 'int' object to str implicitly
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
0
1
2
3
4
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
0
Value of A is 0
1
Value of A is 1
2
Value of A is 2
3
Value of A is 3
4
Value of A is 4
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
0
Value of A is 0
Value of A is 0
1
Value of A is 1
Value of A is 1
2
Value of A is 2
Value of A is 2
3
Value of A is 3
Value of A is 3
4
Value of A is 4
Value of A is 4
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
Hello Python
Hello Python
Hello Python
Hello Python
Hello Python
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
Hello Python:  0
Hello Python:  1
Hello Python:  2
Hello Python:  3
Hello Python:  4
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
Hello Python:  10
Hello Python:  100
Hello Python:  1000
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
>>> 1Can't convert 'int' object to str implicitly
SyntaxError: invalid syntax
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
>>> 'hello'
'hello'
>>> 'hello'
'hello'
>>> 1
1
>>> import numpy as np
>>> from numpy.random import randn
>>> randn()
0.4650279209218923
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
0.5226100747276048
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-0.9328892644754819
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Loop.py", line 27, in <module>
    print (answer)
NameError: name 'answer' is not defined
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-0.29299966755931706
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Loop.py", line 27, in <module>
    print (answer)
NameError: name 'answer' is not defined
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-0.7834654709725121
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Loop.py", line 27, in <module>
    print (answer)
NameError: name 'answer' is not defined
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-1.0329137148016718
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Loop.py", line 27, in <module>
    print (answer)
NameError: name 'answer' is not defined
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-1.549987579612727
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Loop.py", line 27, in <module>
    print (answer)
NameError: name 'answer' is not defined
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-1.1961667560944933
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Loop.py", line 27, in <module>
    print (answer)
NameError: name 'answer' is not defined
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
0.05617042603388739
None
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-1.5350757521780851
None
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
0.6986008509524918
Leass than 1
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-1.0082447476193936
Less than -1
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
1.730598265952554
Greater than 1
>>> 
============ RESTART: C:/Users/a/Desktop/Python Training/Loop.py ============
-0.4090442144682027
Between -1 and 1
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
0
1
2
3
4
5
6
7
8
9
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
0.4
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
0.7
Traceback (most recent call last):
  File "C:/Users/a/Desktop/Python Training/Law_Large_Number.py", line 10, in <module>
    print (count/10)*100
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
90.0
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
650.0
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
6.4
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
66.7
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
67.4
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
688.4
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
0.686
>>> 
====== RESTART: C:/Users/a/Desktop/Python Training/Law_Large_Number.py ======
0.6768
>>> 
