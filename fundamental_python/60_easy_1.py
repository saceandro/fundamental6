#!/usr/bin/env python

import sys
import csv

col = int(raw_input()) - 1
key = raw_input()
print sys.stdin.readline(),
d = csv.reader(sys.stdin)
for l in d:
    if l[col] == key:
        print ','.join(l)
