#!/usr/bin/env python

import sys

def motif_count(seq_name, seq, motif):
    count = 0
    for i in range(len(seq)):
        if seq[i:].startswith(motif):
            count += 1
    print "%s: %d" % (seq_name, count)

motif = raw_input()
seq_name = None
seq = ""

for l in sys.stdin:
    l = l.strip()
    if l.startswith('>'):
        if seq_name is not None:
            motif_count(seq_name, seq, motif)
        seq_name = l[1:].split(' ')[0]
        seq = ""
        continue
    seq += l
motif_count(seq_name, seq, motif)
