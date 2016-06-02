#!/usr/bin/env python

import sys
import re

pat = re.compile("[0-9]+ sequence")
for l in sys.stdin:
    m = pat.search(l)
    if m != None:
        line = m.group(0)
        num_seq = line.split(' ')[0]
        print "%s" % num_seq
