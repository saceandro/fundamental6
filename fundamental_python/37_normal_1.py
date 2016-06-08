#!/usr/bin/env python

dic = {}

while True:
    a = raw_input()
    b = raw_input()
    if a == "END":
        break
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
    if b in dic:
        dic[b] += 1
    else:
        dic[b] = 1

max_num = 0
max_name = None
for k,v in dic.items():
    if v > max_num:
        max_num = v
        max_name = k
print max_name, max_num
