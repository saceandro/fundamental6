#!/usr/bin/env python

from Bio import SeqIO
record = SeqIO.read("NC_001138.gb", "genbank")
output_handle = open("NC_001138_cds.fasta", "w")
count = 0
for feature in record.features:
    if feature.type == "CDS":
        count = count + 1
        # feature_name = "..." # Use feature.qualifiers or feature.dbxrefs here
        feature_seq = feature.extract(record.seq)
        # Simple FASTA output without line wrapping:
        output_handle.write(">" + "\n" + str(feature_seq) + "\n")
output_handle.close()
print(str(count) + " CDS sequences extracted")
