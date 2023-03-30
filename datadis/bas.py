from os import stat
from turtle import st
import numpy
from scipy import stats
speed=numpy.array([10,12,32,42])
x=numpy.mean(speed)
print("mean = ",x)

y=numpy.median(speed)
print("median = ",y)


stnd=numpy.std(speed)
var=numpy.var(speed)
print("S.D = ",stnd,"VARIANCE = ",var)

