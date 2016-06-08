#!/usr/bin/env python

import sys

try:
    with open('test.txt', 'r') as f:
        print len(f.readlines())
        f.close()
except IOError as e:
    print >>sys.stderr, "I/O Error: %s" % e
    print >>sys.stderr, "please check if test.txt exists"
