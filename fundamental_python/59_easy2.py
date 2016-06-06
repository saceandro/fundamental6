#!/usr/bin/env python

import sys
import re

pat = re.compile("([0-9]+) sequence")
for l in sys.stdin:
    m = pat.search(l)
    if m != None:
        print m.group(1)
