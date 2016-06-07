#!/usr/bin/env python

import sys

filename = raw_input()
try:
    with open(filename, "r") as f:
        count = 1
        for l in f.readlines():
            print "%d: %s" % (count, l),
            count += 1
except IOError as e:
    print "ERROR"
