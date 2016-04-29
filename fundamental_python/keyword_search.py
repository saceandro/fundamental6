#!/usr/bin/env python

target_file_name = raw_input()
keyword = raw_input()
out_file_name = raw_input()
try:
    with open(target_file_name, 'r') as targetf:
        with open(out_file_name, 'w') as outf:
            linecount = 1
            hitcount = 1
            for l in targetf.readlines():
                if keyword == 'id':
                    if 'id' in l:
                        print >>outf, "line %d, hit #%d:   %s" % (linecount, hitcount, l),
                        hitcount += 1
                else:
                    words = [word.strip(',.\n') for word in l.split(' ')]
                    if keyword in words:
                        print >>outf, "line %d, hit #%d:   %s" % (linecount, hitcount, l),
                        hitcount += 1
                linecount += 1
except IOError as e:
    print "ERROR"
