'''
This function calculate the Riemann Sum of a customized function (as long as that can be expressed into python code, my assignment was for f(x) = e^(x), but it can always be changable). There are 2 types of Riemann Sum below: the trapezoidal one and the middle rectangle one.
'''

import math
#syntax for e funcion: math.exp(n)

n = 10 #number of trapezoids
a = 1 #lower bound
b = 2 #upper bound
xt = (b-a)/n #delta x, or (b-a)/n
x1 = a
x2 = x1 + xt
T = 0 #a variable for the sum of the trapezoids
M = 0 #a variable for the sum of the rectangles
def f(x):
  return math.exp(1/x) #the function we are integrating

for i in range(n):
  T = T + 1/2*(f(x1)+f(x2))*xt
  x1 = x2
  x2 = x1 + xt

print("T = ", T)

#I'm just reseting the data for M:

n = 10 
a = 1
b = 2 
xt = (b-a)/n #
x1 = a
x2 = x1 + xt

for i in range(n):
  M = M + f((x1+x2)/2)*xt
  x1 = x2
  x2 = x1 + xt

print("M = ", M)