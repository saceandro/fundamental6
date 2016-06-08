#!/usr/bin/env python

import sys, csv

i = int(raw_input()) - 1
j = int(raw_input()) - 1

d = csv.reader(sys.stdin)
for l in d:
    l[i], l[j] = l[j], l[i]
    print ','.join(l)
