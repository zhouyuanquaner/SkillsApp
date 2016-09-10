#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open("/Users/Tammy/Downloads/Skills.csv", 'r')
lines = f.readlines()
f.close()

def process(line):
    line = line.replace('""', '❤')
    stat = 0
    ca = ""
    flag = 0
    fields = []
    res = []
    
    for c in line:
        if stat is 0 and c is '"':
            stat = 1
        elif stat is 0 and c is ',':
            if flag is 1:
                flag = 0
                continue
            fields.append(ca)
            ca = ""
        elif stat is 0:
            ca = ca + c
        elif stat is 1 and c is '"':
            fields.append(ca)
            ca = ""
            stat = 0
            flag = 1
        elif stat is 1:
            ca = ca + c
        else:
            raise Exception("Illegal state")
    res = fields[0:10]
    groups = [(10, 22), (22, 29), (29, 31), (31, 36), (36,41), (41, 48), (48, 57), (57, 58)]
    for group in groups:
        data = fields[group[0]:group[1]]
        aggregation = ','.join([x for x in data if x != ''])
        res.append('"{}"'.format(aggregation))
    return res


def store(line):
    line = process(line)
    line = [l.replace('❤', '""') for l in line]
    #des = open("/Users/Tammy/Desktop/Skills.csv", 'w')
    #write line into des.scv
    print line
    #des.close()

if __name__ == '__main__':
    # for line in lines:
    #     store(line)
    store(lines[88])