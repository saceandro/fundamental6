#!/usr/bin/env python

a = [0] * 10
for i in range(10):
    a[i] = [i]
for j in a:
    j[0] += 10
print a
