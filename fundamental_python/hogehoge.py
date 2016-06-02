#!/usr/bin/env python

class Hogehoge:
    def __init__(self, d):
        self.d = d
    def plus(self, value):
        return self.d + value
    
c = Hogehoge(4)
print c.plus(5)
