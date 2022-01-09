a=0

'''while a < 5:
    print (a)
    print ('Value of A is ' + str(a))
    print ('Value of A is {}'.format(a))
    a = a + 1
'''

'''for i in range(5):
    print("Hello Python")'''

'''mylist = [10,100,1000]

for i in mylist:
    print("Hello Python: ",i)
'''

import numpy as np
from numpy.random import randn

x = randn()
answer= None
if x>1:
    answer = "Greater than 1"
elif x < -1:
    answer = "Less than -1"
else :
    answer = "Between -1 and 1"
print (x)
print (answer)
