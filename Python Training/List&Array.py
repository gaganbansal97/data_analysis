Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mtlist = [1,2,3]
>>> mtlist
[1, 2, 3]
>>> type(mtlist)
<class 'list'>
>>> lsit1 = ['hello',24,True]
>>> lsit1
['hello', 24, True]
>>> l3 = [lsit1,mtlist]
>>> l3
[['hello', 24, True], [1, 2, 3]]
>>> l3[1]
[1, 2, 3]
>>> l3[1][1]
2
>>> range(4)
range(0, 4)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> y = list(range(8))
>>> y
[0, 1, 2, 3, 4, 5, 6, 7]
>>> z = list(range(100,120))
>>> z
[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
>>> w = ['a'.'b','c','d','e']
SyntaxError: invalid syntax
>>> w
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    w
NameError: name 'w' is not defined
>>> w = ['a','b','c','d','e']
>>> w
['a', 'b', 'c', 'd', 'e']
>>> len(w)
5
>>> w[-1]
'e'
>>> w[-4]
'b'
>>> w[-1:-4]
[]
>>> print (w[1:2])
['b']
>>> w[-4:-1]
['b', 'c', 'd']
>>> w[2]=63
>>> w
['a', 'b', 63, 'd', 'e']
>>> w[2:4:2]
[63]
>>> w[1:4:2]
['b', 'd']
>>> w[1:5]
['b', 63, 'd', 'e']
>>> w[0:7]
['a', 'b', 63, 'd', 'e']
>>> w[0:7:8]
['a']
>>> w[0:7:-3]
[]
>>> w[::-3]
['e', 'b']
>>> w[-1:-6:-3]
['e', 'b']
>>> w[4:1:-1]
['e', 'd', 63]
>>> #tuple
>>> t1 = {1,2,3}
>>> t1
{1, 2, 3}
>>> t1[1]=3
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    t1[1]=3
TypeError: 'set' object does not support item assignment
>>> range(20,31)
range(20, 31)
>>> list{range(20,31)}
SyntaxError: invalid syntax
>>> list(range(20,31))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
>>> list1 = list(range(20,31))
>>> len(list1)
11
>>> type(list1)
<class 'list'>
>>> max(list1)
30
>>> 
>>> l = [123,342,455]
>>> import numpy as np
>>> 
>>> np.array(l)
array([123, 342, 455])
>>> a = np.array(l)
>>> a
array([123, 342, 455])
>>> np.array(l,12.3,'abd')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    np.array(l,12.3,'abd')
ValueError: only 2 non-keyword arguments accepted
>>> np.array([l,12.3,'abd'])
array([list([123, 342, 455]), 12.3, 'abd'], dtype=object)
>>> l.p
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    l.p
AttributeError: 'list' object has no attribute 'p'
>>> l.pop()
455
>>> b = np.array([l,12.3,'abd'])
>>> print(b)
[list([123, 342]) 12.3 'abd']
>>> b = a[1:2]
>>> b
array([342])
>>> b = a[0:2]
>>> b
array([123, 342])
>>> b[:]=111
>>> b
array([111, 111])
>>> a
array([111, 111, 455])
>>> #above 4-5 lines are important. If we create copy of array(a) then we make changes in copy of array then oroginal array will also change
>>> c = a.copy()
>>> c[0]=0
>>> c
array([  0, 111, 455])
>>> a
array([111, 111, 455])
>>> 
