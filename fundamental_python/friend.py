#!/usr/bin/env python

dic = {}
while True:
    a = raw_input()
    b = raw_input()
    if a == 'END':
        break
    if a in dic.keys():
        dic[a] += 1
    else:
        dic[a] = 1
    if b in dic.keys():
        dic[b] += 1
    else:
        dic[b] = 1

m = 0
n = ''
for name in dic.keys():
    if m < dic[name]:
        m = dic[name]
        n = name
print "%s %d" % (n, m)
