import random
import numpy as np
import math
a = int(input("Enter the lower limit of x, a: "))
b = int(input("Enter the upper limit of x, b: "))
sDev = int(input("Enter the standard deviation: "))
mean = int(input("Enter mean: "))
N = int(input("Enter the number of random points N: "))
 
#generates N random points as an array included 0's
RandomPts = np.zeros(N)
for i in range(len(RandomPts)):#N times looped
    #generates uniformly distributed random points between a and b
    RandomPts[i]=random.uniform(a,b)

#calculates the value of f(x)
def fVal(x):
    f = ((1/(sDev*math.sqrt(2*math.pi)))*(math.exp(-((math.pow(x-mean,2))/8))))
    return f
#variance = fmax = h
h=sDev**2
#initial value of randomly generated N points under curve nIn
nIn=0.0

for i in range(N):
    x=random.uniform(a,b)
    y=random.uniform(0,h)
    if(y<=fVal(RandomPts[i])):
        nIn+=1
#result of estimated value of I
Iest=(b-a)*float(h)*(nIn/N)
print("The result of estimation of area under curve I is:\t",Iest)
