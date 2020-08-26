import random
import math

length = int(input("Enter the length of a needle l: "))
n = int(input("Enter the total number of needles n: "))

#number of needles that falls onto a line
h=0
for i in range(n):
    Q=random.uniform(0,math.pi)
    d=random.uniform(0,length/2)
    if(d<(length/2*math.sin(Q))):
        h+=1
        #print("needle is on a line!")
    else:
        h+=0
        #print("needle is not on a line")
#estimating the value of pi
ProbabilityOfNeedleOntoLine=h/n
TotalArea=(math.pi*length)/2
Area=(((-length)/2)*math.cos(math.pi))+(((length)/2)*math.cos(0))
ProbabilityOfNeedleOntoArea=Area/TotalArea

ValOfPi=(2*n)/h
print("Estimated Value of Pi: ",ValOfPi)
