#!/usr/bin/env python

class Foo:
    def __init__(self, name):
        self.name = name
        
    def hello(self):
        print "Hello, " + self.name + "!"

    def googbye(self):
        print "Good-bye, " + self.name + "!"

a = Foo("hogehoge")
a.hello()
a.googbye()

b = Foo("John")
b.hello()
b.googbye()
