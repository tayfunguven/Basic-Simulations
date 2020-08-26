import random
import numpy as np
import math

a = int(input("Enter the lower limit of x, a: "))
b = int(input("Enter the upper limit of x, b: "))
sDev = int(input("Enter the standard deviation: "))
mean = int(input("Enter mean: "))
N = int(input("Enter the number of random points N: "))

xrand = np.zeros(N)
Total=0.0
TotalFsquare=0.0
#obtain N random points xi in [a,b]
for i in range(len(xrand)):
    xrand[i]=random.uniform(a,b)
    #calculate F(xi) for each point xi
    f = ((1/(sDev*math.sqrt(2*math.pi)))*(math.exp(-((math.pow(xrand[i]-mean,2))/8))))
    Total+=f
    #calculate F(xi)^2 for each point xi
    fsquare= ((1/(sDev*math.sqrt(2*math.pi)))*(math.exp(-((math.pow(xrand[i]-mean,2))/8))))
    TotalFsquare+=fsquare

#take average
Average = Total/N
#take squared average
AverageFsquare=TotalFsquare/N
#result of estimated value of I
Iest=(b-a)*Average
#result of statistical error involved MC
IestErr=AverageFsquare-math.pow(Average,2)
print("\nThe result of estimation of area under curve I is:\t",Iest)
print("Statistical error involed in MC:\t", IestErr, "\n")
