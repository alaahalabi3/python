import numpy as np
from numpy.random import randn

#This is to test that each time we make N larger we get an accurate number close to 68.2%
counter  = 0
n =100000

for i in randn(n):
    if (i > -1 and i < 1):
        counter = counter + 1
        
        
print(counter/n)
        
