import math
import numpy
import scipy
from matplotlib import pylab
from scipy import optimize

def f(i):
    return numpy.sin(i/5)*numpy.exp(i/10)+5*numpy.exp(-i/2)
def f1(x):
    return [x**0, x**1]
def f2(x):
    return [x**0, x**1, x**2]
def f3(x):
    return [x**0, x**1, x**2, x**3]


A1 = numpy.array([f1(1), f1(15)])
A2 = numpy.array([f2(1), f2(8), f2(15)])
A3 = numpy.array([f3(1), f3(4), f3(10), f3(15)])

B1 = numpy.array([[f(1)], [f(15)]])
B2 = numpy.array([[f(1)], [f(8)], [f(15)]])
B3 = numpy.array([[f(1)], [f(4)], [f(10)], [f(15)]])

r1 = numpy.linalg.solve(A1, B1)
r2 = numpy.linalg.solve(A2, B2)
r3 = numpy.linalg.solve(A3, B3)

print((optimize.minimize(f, 2, method='BFGS')).fun)