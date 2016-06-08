#!/usr/bin/env python

import sys, re

pat = re.compile(" (\d+) sequence")

for l in sys.stdin:
    m = pat.search(l)
    if m != None:
        print m.group(1)
