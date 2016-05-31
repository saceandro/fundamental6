#!/usr/bin/env python

infile_name = raw_input()
keyword = raw_input()
outfile_name = raw_input()

with open(infile_name, "r") as infile:
    with open(outfile_name, "w") as outfile:
        lines = infile.readlines()
        hitcount = 1
        for i in range(len(lines)):
            if keyword == "id":
                if lines[i].find(keyword) != -1:
                    outfile.write("line %d, hit #%d:   %s" % (i+1, hitcount, lines[i]))
                    hitcount += 1
            # else:
            #     items = lines[i].split(" ")
            #     hitcount_num = 0
            #     for item in items:
            #         if item.find(keyword) != -1:
            #             hitcount_num += 1
            #     if hitcount_num > 0:
            #         outfile.write("line %d, hit #%d:   %s" % (i+1, hitcount, lines[i]))
            #         hitcount += hitcount_num
            else:
                items = [item.strip(",.\n") for item in lines[i].split(" ")]
                if keyword in items:
                    outfile.write("line %d, hit #%d:   %s" % (i+1, hitcount, lines[i]))
                    hitcount += 1
        outfile.close()
    infile.close()
