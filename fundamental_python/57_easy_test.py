#!/usr/bin/env python

import sys
import re

pat = re.compile("Chr \w+")

for l in sys.stdin:
    if l.startswith('>'):
        gene = l.split(' ')[1]
        chrom = None
        m = pat.search(l)
        if m != None:
            chrom = m.group(0)
        else:
            chrom = "plasmid"
        print "%s,%s" % (gene, chrom)
