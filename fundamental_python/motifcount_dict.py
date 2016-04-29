#!/usr/bin/env python

import sys

def motif_count(seq_name, seq, motif, dic):
    count = 0
    for i in range(len(seq)):
        if seq[i:].startswith(motif):
            count += 1
    dic[seq_name] = count
    
motif = raw_input()
seq_name = None
seq = ""
dic = {}

for l in sys.stdin:
    l = l.strip()
    # print "'%s'" % l,
    if l.startswith('>'):
        if seq_name is not None:
            motif_count(seq_name, seq, motif, dic)
        seq_name = l[1:].split(' ')[0]
        seq = ""
        continue
    seq += l
motif_count(seq_name, seq, motif, dic)

for k, v in dic.items():
    print "%s: %d" % (k, v)
