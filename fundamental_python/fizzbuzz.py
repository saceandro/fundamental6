#!/usr/bin/env python

print "Input a number>"
n = raw_input()
ni = int(n)

for i in range(1, ni+1):
    if i%3 == 0 and i%5 == 0:
        print "FizzBuzz"
    elif i%3 == 0:
        print "Fizz"
    elif i%5 == 0:
        print "Buzz"
    else:
        print i
