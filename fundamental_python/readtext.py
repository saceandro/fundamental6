#!/usr/bin/env python

import sys

try:
    with open('test.txt', 'r') as f:
        print len(f.readlines())
except IOError as e:
    print >>sys.stderr, "I/O Error:", e
    print >>sys.stderr, "test.txt does not exist"
