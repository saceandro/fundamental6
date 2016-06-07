#!/usr/bin/env python

import sys
import csv

file1 = raw_input()
file2 = raw_input()
dic = {}

try:
    with open(file1, "r") as f1:
        d1 = csv.reader(f1, delimiter='\t')
        for l in d1:
            dic[l[0]] = l[1]
            
        with open(file2, "r") as f2:
            d2 = csv.reader(f2, delimiter='\t')
            for l in d2:
                print '\t'.join(l) + "\t" + dic[l[0]]
            f2.close()
        f1.close()
except IOError as e:
    print >>sys.stderr, "I/O Error:", e
