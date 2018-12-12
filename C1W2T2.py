import numpy
import scipy
from matplotlib import pylab

def f(i):
    return numpy.sin(i/5)*numpy.exp(i/10)+5*numpy.exp(-i/2)
def f1(x):
    return [x**0, x**1]
def f2(x):
    return [x**0, x**1, x**2]
def f3(x):
    return [x**0, x**1, x**2, x**3]

#!
x1 = [1, 15]
x2 = [1, 10, 15]
x3 = [1, 4, 8, 15]

A1 = numpy.array([f1(1), f1(15)])
A2 = numpy.array([f2(1), f2(8), f2(15)])
A3 = numpy.array([f3(1), f3(4), f3(10), f3(15)])

B1 = numpy.array([[f(1)], [f(15)]])
B2 = numpy.array([[f(1)], [f(8)], [f(15)]])
B3 = numpy.array([[f(1)], [f(4)], [f(10)], [f(15)]])

r1 = numpy.linalg.solve(A1, B1)
r2 = numpy.linalg.solve(A2, B2)
r3 = numpy.linalg.solve(A3, B3)

#test plot
test_x = numpy.arange(1, 15, 0.1)
test_f = []
for item in test_x:
    test_f.append(f(item))
#pylab.plot(test_x, f(test_x))

# #test map
# test_x = [1, 8, 15]
# test_map = map(f, test_x)
# print(test_map)

pylab.plot(test_x, test_f, x1, r1, x2, r2, x3, r3)
pylab.show()
print(float(r1[0]), float(r1[1]))
print(float(r2[0]), float(r2[1]), float(r2[2]))
print(float(r3[0]), float(r3[1]), float(r3[2]), float(r3[3]))