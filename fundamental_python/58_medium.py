#!/usr/bin/env python

import re
def check_hit(p, s):
    r = p.search(s)
    if r == None:
        print "0"
    else:
        print "1"
pat = re.compile(r"(^AB|C)D(E|F$)")
check_hit(pat, "ABDENC")

check_hit(pat, "ABDFC")

check_hit(pat, "ABDX")

check_hit(pat, "CDEX")

check_hit(pat, "CDFX")

check_hit(pat, "NCDEX")

check_hit(pat, "NCDFX")

check_hit(pat, "NABDE")

check_hit(pat, "NABDF")
