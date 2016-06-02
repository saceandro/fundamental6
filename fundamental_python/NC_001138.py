#!/usr/bin/env python

import sys
import json
import re

complement = {'a':'t', 'c':'g', 'g':'c', 't':'a'}
pat = re.compile("(?P<start>[0-9]+)<?>?\.\.<?>?(?P<end>[0-9]+)")

dat = json.load(sys.stdin)[0]

for i in dat["features"]:
    if i["feature"] == "CDS":
        print >>sys.stderr, i["position"]
        m = re.findall(pat, i["position"])
        for l in m:
            print >> sys.stderr, "%d\t%d" % (int(l[0]), int(l[1]))
        # print >>sys.stderr, m
        print >>sys.stderr
        print ">%s" % i["locus_tag"][0]
        if i["position"].startswith("complement"):
            fasta = ''.join(''.join(complement.get(base) for base in reversed(dat["sequence"][int(l[0])-1:int(l[1])])) for l in m).upper()
        else:
            fasta = ''.join((dat["sequence"][int(l[0])-1:int(l[1])]) for l in m).upper()
        for j in range(0, len(fasta), 70):
            print fasta[j:j+70]
