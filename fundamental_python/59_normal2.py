#!/usr/bin/env python

import sys
import re

pat1 = re.compile("<A HREF=\"#[^<>]+\">(<em>)?(?P<name>[^<>]+)(</em>)?</A>\n")

def extract_species():
    for l in sys.stdin:
        if l.strip() == "<FONT color=\"#006666\"><B>VERTEBRATES - Sequence downloads only</B></FONT>":
            break
        m = pat1.search(l)
        if m != None:
            print m.group('name')

for l in sys.stdin:
    if l.strip() == "<FONT color=\"#006666\"><B>VERTEBRATES - Complete annotation sets</B></FONT>":
        extract_species()
