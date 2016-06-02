#!/usr/bin/env python

import sys

col = int(raw_input()) - 1
key = raw_input()
print sys.stdin.readline(),
for l in sys.stdin:
    l = l.rstrip('\n').split(',')
    if l[col] == key:
        print ','.join(l)
