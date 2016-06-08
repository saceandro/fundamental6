#!/usr/bin/env python

import sys, csv

d = csv.reader(sys.stdin, delimiter='\t')

dic = {}
for l in d:
    if l[0].startswith("211") or l[0].startswith("Unmapped"):
        continue
    if l[2] == "gene":
        if l[0] in dic:
            dic[l[0]][0] += 1
            dic[l[0]][1] = (1.0 - 1.0/dic[l[0]][0]) * dic[l[0]][1] + 1.0/dic[l[0]][0] * (long(l[4]) - long(l[3]) + 1)
        else:
            dic[l[0]] = [1, long(l[4]) - long(l[3]) + 1]

ks = dic.keys()
ks.sort()
print "Chromosome,Gene Count,Avg Size"
for k in ks:
    print "%s\t%d\t%d" % (k, long(dic[k][0]), long(dic[k][1]))
