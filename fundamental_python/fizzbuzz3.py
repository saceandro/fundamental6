#!/usr/bin/env python

import sys

if len(sys.argv) <= 1:
    print "Usage: fizzbuzz2 <number>"
    sys.exit(1)

ni = int(sys.argv[1])

for i in range(1, ni+1):
    if i%3 == 0 and i%5 == 0:
        print "FizzBuzz"
    elif i%3 == 0:
        print "Fizz"
    elif i%5 == 0:
        print "Buzz"
    else:
        print i

