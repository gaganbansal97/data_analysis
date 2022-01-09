Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> mydata = np.arange(0,20)
>>> mydata
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])
>>> np.reshape(mydata,(5,4))
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
>>> np.reshape(mydata,(5,4),F)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    np.reshape(mydata,(5,4),F)
NameError: name 'F' is not defined
>>> np.reshape(mydata,(5,4),order = 'F')
array([[ 0,  5, 10, 15],
       [ 1,  6, 11, 16],
       [ 2,  7, 12, 17],
       [ 3,  8, 13, 18],
       [ 4,  9, 14, 19]])
>>> np.reshape(mydata,(5,4),order = 'C')
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
>>> mat = np.reshape(mydata,(5,4),order = 'C')
>>> mat[2][2]
10
>>> mat1 = np.reshape(mydata,(5,4),order = 'F')
>>> mat1[2][2]
12
>>> np.transpose(mat)
array([[ 0,  4,  8, 12, 16],
       [ 1,  5,  9, 13, 17],
       [ 2,  6, 10, 14, 18],
       [ 3,  7, 11, 15, 19]])
>>> mat
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
>>> type(mydata)
<class 'numpy.ndarray'>
>>> type(mat)
<class 'numpy.ndarray'>
>>> #--------------------------------------
>>> r1 = ['a','b','c']
>>> r2 = [1,2,3]
>>> np.array([r1,r2])
array([['a', 'b', 'c'],
       ['1', '2', '3']],
      dtype='<U1')
>>> print(np.array(r1,r2))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(np.array(r1,r2))
TypeError: data type not understood
>>> print(np.array([r1,r2]))
[['a' 'b' 'c']
 ['1' '2' '3']]
>>> # DICTIONARIES ----------------------
>>> # ---------------------------------
>>> # DICTIONARIES ----------------------
>>> # ---------------------------------
>>> mat[1]
array([4, 5, 6, 7])
>>> mat[1][-1]
7
>>> mat[1,-1]
7
>>> dict1 = {'a1':'val1','b1':'val2'}
>>> dict1
{'a1': 'val1', 'b1': 'val2'}
>>> dict1['b1']
'val2'
>>> dict1['a1']
'val1'
>>> dict1[1]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict1[1]
KeyError: 1
>>> dict2 = {'Germany':"Europe","India":"Asia"}
>>> dict2
{'Germany': 'Europe', 'India': 'Asia'}
>>> dict2 = {'Germany':"Europe","India":"Asia","Australia":2}
>>> dict2
{'Germany': 'Europe', 'India': 'Asia', 'Australia': 2}
>>> 
 RESTART: C:/Users/a/Desktop/Python Training/Basket_Ball_Trends/BasketBall Data.py 
>>> 
