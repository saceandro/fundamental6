#!/usr/bin/env python

fname = raw_input()
try:
    with open(fname, 'r') as f:
        lines = f.readlines()
        l = len(lines)
        for i in range(l):
            print "%d: %s" % (i+1, lines[i]),
except IOError as e:
    print "ERROR"
