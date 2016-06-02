#!/usr/bin/env python

import sys
import csv
dic = {}
d = csv.reader(sys.stdin, delimiter='\t')
for l in d:
    if l[0].startswith('211') or l[0].startswith('Unmapped'):
        continue
    if l[0] in dic:
        dic[l[0]][0] += 1
        dic[l[0]][1] = (1.0 - 1.0/dic[l[0]][0]) * dic[l[0]][1] + 1.0/dic[l[0]][0] * (int(l[4]) - int(l[3]) + 1)
    else:
        dic[l[0]] = [1, int(l[4]) - int(l[3]) + 1]
print "Chromosome,Gene Count,Avg Size"
ks = dic.keys()
ks.sort()
for key in ks:
    print "%s\t%d\t%d" % (key, dic[key][0], int(dic[key][1]))
