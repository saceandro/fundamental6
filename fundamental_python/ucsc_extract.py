#!/usr/bin/env python

import sys
import re

pat1 = re.compile("<A HREF=\"#.+\"><em>(.+)</em></A>\n")
pat2 = re.compile("<A HREF=\"#.+\">(.+)</A>\n")

def extract_species():
    for l in sys.stdin:
        if l.strip() == "<FONT color=\"#006666\"><B>VERTEBRATES - Sequence downloads only</B></FONT>":
            break
        m = pat1.search(l)
        if m != None:
            species = m.group(1)
            print "%s" % species
        else:
            m = pat2.search(l)
            if m != None:
                species = m.group(1)
                print "%s" % species

for l in sys.stdin:
    if l.strip() == "<FONT color=\"#006666\"><B>VERTEBRATES - Complete annotation sets</B></FONT>":
        extract_species()
