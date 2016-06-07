#!/usr/bin/env python

import sys
import csv

d = csv.reader(sys.stdin)
content = []
csv_content = []
spaces = []
max_newline = []
count = 0
line_count = 0
newline_count = 0
for l in d:
    max_newline.append(0)
    csv_content.append(l)
    if len(spaces) == 0:
        spaces = [0] * len(l)
    maxsplit = 0
    for j in range(len(l)):
        # print l[j]
        # if l[j] != '':
        #     print '\t'.join(l[j].split("\r"))
        cell = l[j].split("\r")
        if len(cell) > maxsplit:
            maxsplit = len(cell)
        if len(cell) > max_newline[count]:
            max_newline[count] = len(cell)
            curr_cell_max_space = max(len(i) for i in cell) + 3
            if curr_cell_max_space > spaces[j]:
                spaces[j] = curr_cell_max_space
    newline_count += max_newline[count]
    
    for k in range(maxsplit):
        content.append(['0']*len(l))

    for j in range(len(l)):
        cell = l[j].split("\r")
        # print len(cell)
        for k in range(len(cell)):
            content[line_count + k][j] = cell[k]
        if len(cell) < maxsplit:
            for k in range(len(cell) - 1, maxsplit):
                content[line_count + k][j] = ''
        # if l[j] != '':
        #     print '\t'.join(l[j].split("\r"))
            # if len(cell) > maxsplit:
            #     maxsplit = len(cell)
            # if len(cell) > max_newline[count]:
            #     max_newline[count] = len(cell)
            #     curr_cell_max_space = max(len(i) for i in cell) + 3
            #     if curr_cell_max_space > spaces[j]:
            #         spaces[j] = curr_cell_max_space
    count += 1
    line_count += maxsplit
    # line = []
    # for i in len(l):
    #     l[i].split("\r")
    # print '\t'.join(item.replace("\r", "\n") for item in l)

# width = 1 + sum(spaces)
# print '-' * width
# for l in csv_content:
#     for j in range(len(l)):
#         sys.stdout.write('| ')
#         sys.stdout.write(l[j] + ' ' * (spaces[j] - len(l[j]) - 3))
#         sys.stdout.write(' ')
#     print ' '
for i in content:
    for j in i:
        print "%s\t" % j,
    print
