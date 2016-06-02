#!/usr/bin/env python

import sys
import csv

col1 = int(raw_input()) - 1
col2 = int(raw_input()) - 1

for l in sys.stdin:
    l = l.rstrip('\n').split(',')
    a = l[col1]
    l[col1] = l[col2]
    l[col2] = a
    print ','.join(l)
