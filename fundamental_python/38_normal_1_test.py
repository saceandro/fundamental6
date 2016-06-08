#!/usr/bin/env python

import sys

fname = raw_input()

try:
    with open(fname, 'r') as f:
        count = 1
        for l in f.readlines():
            print "%d: %s" % (count, l),
            count += 1
        f.close()
except IOError as e:
    print "ERROR"
