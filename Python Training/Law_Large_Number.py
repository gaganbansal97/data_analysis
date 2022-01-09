import numpy
from numpy.random import randn
count = 0
N=10000
for i in randn(N):
    
    if i < 1 and i > -1:
        count = count + 1

print ((count/N))
