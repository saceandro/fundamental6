#!/usr/bin/env python

for i in range(1, 4):
    print "#",
    for j in range(1, 4):
        if i == j:
            print " ",
            continue
        print "%d" % j,
    print "#"
