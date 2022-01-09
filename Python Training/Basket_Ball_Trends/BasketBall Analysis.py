Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/a/Desktop/Python Training/Basket_Ball_Trends/BasketBall Data.py 
>>> pdict["LeBronJames"]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pdict["LeBronJames"]
NameError: name 'pdict' is not defined
>>> Pdict["LeBronJames"]
2
>>> FieldGoals
array([[978, 813, 775, 800, 716, 740, 574, 738,  31, 266],
       [632, 536, 647, 620, 635, 514, 423, 445, 462, 446],
       [875, 772, 794, 789, 768, 758, 621, 765, 767, 624],
       [756, 691, 728, 535, 688, 684, 441, 669, 743, 358],
       [468, 526, 583, 560, 510, 619, 416, 470, 473, 251],
       [549, 543, 507, 615, 600, 524, 393, 485, 492, 343],
       [407, 381, 630, 631, 314, 430, 425, 412, 406, 568],
       [306, 306, 587, 661, 794, 711, 643, 731, 849, 238],
       [208, 208, 208, 574, 672, 711, 302,   0,  58, 338],
       [699, 472, 439, 854, 719, 692, 416, 569, 415, 509]])
>>> Games
array([[80, 77, 82, 82, 73, 82, 58, 78,  6, 35],
       [82, 57, 82, 79, 76, 72, 60, 72, 79, 80],
       [79, 78, 75, 81, 76, 79, 62, 76, 77, 69],
       [80, 65, 77, 66, 69, 77, 55, 67, 77, 40],
       [82, 82, 82, 79, 82, 78, 54, 76, 71, 41],
       [70, 69, 67, 77, 70, 77, 57, 74, 79, 44],
       [78, 64, 80, 78, 45, 80, 60, 70, 62, 82],
       [35, 35, 80, 74, 82, 78, 66, 81, 81, 27],
       [40, 40, 40, 81, 78, 81, 39,  0, 10, 51],
       [75, 51, 51, 79, 77, 76, 49, 69, 54, 62]])
>>> FieldGoals/Games

Warning (from warnings module):
  File "C:/Users/a/Desktop/Python Training/Basket_Ball_Trends/BasketBall Data.py", line 1
    #Dear Student,
RuntimeWarning: invalid value encountered in true_divide
array([[ 12.225     ,  10.55844156,   9.45121951,   9.75609756,
          9.80821918,   9.02439024,   9.89655172,   9.46153846,
          5.16666667,   7.6       ],
       [  7.70731707,   9.40350877,   7.8902439 ,   7.84810127,
          8.35526316,   7.13888889,   7.05      ,   6.18055556,
          5.84810127,   5.575     ],
       [ 11.07594937,   9.8974359 ,  10.58666667,   9.74074074,
         10.10526316,   9.59493671,  10.01612903,  10.06578947,
          9.96103896,   9.04347826],
       [  9.45      ,  10.63076923,   9.45454545,   8.10606061,
          9.97101449,   8.88311688,   8.01818182,   9.98507463,
          9.64935065,   8.95      ],
       [  5.70731707,   6.41463415,   7.1097561 ,   7.08860759,
          6.2195122 ,   7.93589744,   7.7037037 ,   6.18421053,
          6.66197183,   6.12195122],
       [  7.84285714,   7.86956522,   7.56716418,   7.98701299,
          8.57142857,   6.80519481,   6.89473684,   6.55405405,
          6.2278481 ,   7.79545455],
       [  5.21794872,   5.953125  ,   7.875     ,   8.08974359,
          6.97777778,   5.375     ,   7.08333333,   5.88571429,
          6.5483871 ,   6.92682927],
       [  8.74285714,   8.74285714,   7.3375    ,   8.93243243,
          9.68292683,   9.11538462,   9.74242424,   9.02469136,
         10.48148148,   8.81481481],
       [  5.2       ,   5.2       ,   5.2       ,   7.08641975,
          8.61538462,   8.77777778,   7.74358974,          nan,
          5.8       ,   6.62745098],
       [  9.32      ,   9.25490196,   8.60784314,  10.81012658,
          9.33766234,   9.10526316,   8.48979592,   8.24637681,
          7.68518519,   8.20967742]])
>>> import warnings
>>> warnings.filterwarnings('ignore')
>>> import numpy as np
>>> np.matrix.round(FieldGoals / Games)
array([[ 12.,  11.,   9.,  10.,  10.,   9.,  10.,   9.,   5.,   8.],
       [  8.,   9.,   8.,   8.,   8.,   7.,   7.,   6.,   6.,   6.],
       [ 11.,  10.,  11.,  10.,  10.,  10.,  10.,  10.,  10.,   9.],
       [  9.,  11.,   9.,   8.,  10.,   9.,   8.,  10.,  10.,   9.],
       [  6.,   6.,   7.,   7.,   6.,   8.,   8.,   6.,   7.,   6.],
       [  8.,   8.,   8.,   8.,   9.,   7.,   7.,   7.,   6.,   8.],
       [  5.,   6.,   8.,   8.,   7.,   5.,   7.,   6.,   7.,   7.],
       [  9.,   9.,   7.,   9.,  10.,   9.,  10.,   9.,  10.,   9.],
       [  5.,   5.,   5.,   7.,   9.,   9.,   8.,  nan,   6.,   7.],
       [  9.,   9.,   9.,  11.,   9.,   9.,   8.,   8.,   8.,   8.]])
>>> FieldGoalsPerGame = np.matrix.round(FieldGoals / Games)
>>> FieldGoalsPerGame[Pdict["KobeBryant"]][Sdict["2009"]]
10.0
>>> np.matrix.round(MinutesPlayed / Games)
array([[ 41.,  41.,  39.,  36.,  39.,  34.,  38.,  39.,  30.,  34.],
       [ 41.,  41.,  41.,  40.,  38.,  35.,  35.,  37.,  33.,  35.],
       [ 43.,  41.,  40.,  38.,  39.,  39.,  38.,  38.,  38.,  36.],
       [ 37.,  38.,  36.,  34.,  38.,  36.,  34.,  37.,  39.,  36.],
       [ 37.,  37.,  38.,  36.,  35.,  38.,  38.,  36.,  34.,  30.],
       [ 39.,  39.,  36.,  38.,  36.,  36.,  35.,  33.,  32.,  35.],
       [ 36.,  37.,  38.,  38.,  38.,  36.,  36.,  33.,  35.,  35.],
       [ 36.,  36.,  35.,  39.,  40.,  39.,  39.,  39.,  39.,  34.],
       [ 29.,  29.,  29.,  37.,  37.,  37.,  35.,  nan,  31.,  30.],
       [ 39.,  38.,  38.,  39.,  36.,  37.,  33.,  35.,  33.,  32.]])
>>> #----------------------------------------------
>>> # ------------------  VISUALISATIONS -----------------
>>> #----------------------------------------------
>>> import matplotlib.pylot as plt
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    import matplotlib.pylot as plt
ImportError: No module named 'matplotlib.pylot'
>>> import matplotlib
>>> import matplotlib as plt
>>> plt.plot(Salary[0])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    plt.plot(Salary[0])
AttributeError: module 'matplotlib' has no attribute 'plot'
>>> import matplotlib.pylot as plt
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    import matplotlib.pylot as plt
ImportError: No module named 'matplotlib.pylot'
>>> import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-10 , 10, 100)
y = np.sin(x) 
plt.plot(x, y, marker="x")
plt.show()
SyntaxError: multiple statements found while compiling a single statement
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    import matplotlib.pyplot as plt
  File "C:\Program Files\Python 3.5\lib\site-packages\matplotlib\pyplot.py", line 32, in <module>
    import matplotlib.colorbar
  File "C:\Program Files\Python 3.5\lib\site-packages\matplotlib\colorbar.py", line 30, in <module>
    import matplotlib.collections as collections
  File "C:\Program Files\Python 3.5\lib\site-packages\matplotlib\collections.py", line 19, in <module>
    from . import (_path, artist, cbook, cm, colors as mcolors, docstring,
  File "C:\Program Files\Python 3.5\lib\site-packages\matplotlib\lines.py", line 208, in <module>
    @cbook._define_aliases({
AttributeError: module 'matplotlib.cbook' has no attribute '_define_aliases'
>>> import matplotlib.pylot as plt
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    import matplotlib.pylot as plt
ImportError: No module named 'matplotlib.pylot'
>>> import matplotlib.pylot as plt
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    import matplotlib.pylot as plt
ImportError: No module named 'matplotlib.pylot'
>>> import matlplotlib
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    import matlplotlib
ImportError: No module named 'matlplotlib'
>>> import matplotlib
>>> import matplotlib as plt
>>> plt.plot(Salary[0])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    plt.plot(Salary[0])
AttributeError: module 'matplotlib' has no attribute 'plot'
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    import matplotlib.pyplot as plt
  File "C:\Program Files\Python 3.5\lib\site-packages\matplotlib\pyplot.py", line 32, in <module>
    import matplotlib.colorbar
  File "C:\Program Files\Python 3.5\lib\site-packages\matplotlib\colorbar.py", line 30, in <module>
    import matplotlib.collections as collections
  File "C:\Program Files\Python 3.5\lib\site-packages\matplotlib\collections.py", line 19, in <module>
    from . import (_path, artist, cbook, cm, colors as mcolors, docstring,
  File "C:\Program Files\Python 3.5\lib\site-packages\matplotlib\lines.py", line 208, in <module>
    @cbook._define_aliases({
AttributeError: module 'matplotlib.cbook' has no attribute '_define_aliases'
>>> import matplotlib as plt
>>> Salary[0]
array([15946875, 17718750, 19490625, 21262500, 23034375, 24806250,
       25244493, 27849149, 30453805, 23500000])
>>> %matplotlib inline
SyntaxError: invalid syntax
>>> plt.plot(Salary[0])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    plt.plot(Salary[0])
AttributeError: module 'matplotlib' has no attribute 'plot'
>>> np.plot(Salary[0])
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    np.plot(Salary[0])
AttributeError: module 'numpy' has no attribute 'plot'
>>> print(1)








