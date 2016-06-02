#!/usr/bin/env python

from Bio import SeqIO

for seq_record in SeqIO.parse("NC_001138.gb","genbank"):
    seq_record.features = [f for f in seq_record.features if f.type == "CDS"]
    SeqIO.write(seq_record, "NC_001138.cds.gb", "genbank")
