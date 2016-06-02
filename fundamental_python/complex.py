#!/usr/bin/env python

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im
        
    def __str__(self):
        if self.im < 0:
            return str(self.re) + str(self.im) + "i"
        else:
            return str(self.re)+ "+" + str(self.im) + "i"

# c = Complex(3, 4)
# d = Complex(-1, -2)
# print str(c)
# print str(d)
