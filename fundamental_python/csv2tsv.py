#!/usr/bin/env python

import sys
import csv

d = csv.reader(sys.stdin)
for l in d:
    print '\t'.join(l)
