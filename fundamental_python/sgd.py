#!/usr/bin/env python

import sys
import re

pat = re.compile("Chr [A-Za-z]+")
for l in sys.stdin:
    if l.startswith('>'):
        items = l.split(',')
        gene = items[0].split(' ')[1]
        chrom = None
        m = pat.search(items[1])
        if m != None:
            chrom = m.group(0)
        else:
            chrom = "plasmid"
        print "%s,%s" % (gene, chrom)
