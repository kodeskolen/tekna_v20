# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:27:58 2020

@author: Marie
"""


from pylab import plot, arange, show

# vi ønsker å plotte funksjonen
# f(x) = x^2 - 2x + 5
# fra x = 0 til x = 20

def f(x):
    return x**2 - 2*x + 5

x_verdier = arange(0, 20, 0.5)
print(x_verdier)

y_verdier = f(x_verdier)

print(y_verdier)

plot(x_verdier, y_verdier)
show()