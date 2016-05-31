#!/usr/bin/env python
import re
pat = re.compile(r"^(\d+)$", re.MULTILINE)
print "START"
for r in pat.finditer("123\n45\n678"):
    print r.group(1)
print "END"
