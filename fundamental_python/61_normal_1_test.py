#!/usr/bin/env python

import sys, csv

file1 = raw_input()
file2 = raw_input()

dic = {}
try:
    with open(file1, 'r') as f1:
        d = csv.reader(f1, delimiter='\t')
        for l in d:
            dic[l[0]] = l[1]
        f1.close()
    with open(file2, 'r') as f2:
        d = csv.reader(f2, delimiter='\t')
        for l in d:
            print '\t'.join(l) + '\t%s' % dic[l[0]]
except IOError as e:
    print >>sys.stderr, "I/O Error: %s" % e
