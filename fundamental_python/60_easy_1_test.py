#!/usr/bin/env python

import sys, csv

column = int(raw_input()) - 1
val = raw_input()

print sys.stdin.readline(),

d = csv.reader(sys.stdin)
for l in d:
    if l[column] == val:
        print ','.join(l)
