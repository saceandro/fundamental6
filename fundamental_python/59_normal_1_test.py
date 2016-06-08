#!/usr/bin/env python

import sys, re

pat = re.compile("<A HREF=\"#.+\">(<em>)?(?P<species>.+?)(</em>)?</A>")

for l in sys.stdin:
    if re.search("<FONT color=\"#006666\"><B>VERTEBRATES - Complete annotation sets</B></FONT>", l) != None:
        break
for l in sys.stdin:
    if re.search("<FONT color=\"#006666\"><B>VERTEBRATES - Sequence downloads only</B></FONT>", l) != None:
        break
    m = pat.search(l)
    if m != None:
        print m.group("species")
