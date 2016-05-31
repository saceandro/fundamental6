#!/usr/bin/env python

import sys
import json

jso = ''.join(map(lambda line: line.strip(), sys.stdin.readlines()))
dat = json.loads(jso)
if len(dat) > 0:
    print "TITLE: %s" % dat[0]["title"]
    print "AUTHORS: %s" % ', '.join(dat[0]["authors"])
    for line in dat[1:]:
        print
        print "TITLE: %s" % line["title"]
        print "AUTHORS: %s" % ', '.join(line["authors"])
