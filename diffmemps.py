#!/usr/bin/env python

import sys
import os
import csv

class MemObject():
    def __init__(self, line):
        meta = [ l for l in line.split(' ') if l != '' ]
        self._s_code = meta[0]
        self._s_data = meta[1]
        self._p_code = meta[2]
        self._p_data = meta[3]
        self._sum = 0
        for m in meta[0:3]:
            self._sum += int(m)
        self._addr = meta[4]
        self._name = meta[5]

    @property
    def sum(self):
        return self._sum

    @property
    def s_code(self):
        return self._s_code

    @property
    def s_data(self):
        return self._s_data

    @property
    def p_code(self):
        return self._p_code

    @property
    def p_data(self):
        return self._p_data

    @property
    def addr(self):
        return self._addr

    @property
    def name(self):
        return self._name


def parse_maps(proc_path):
    parse_data = {}
    with open(proc_path) as f:
        lines = [l.strip('\n') for l in f.readlines() if l != '\n']
        for l in lines[2:]:
            mem = MemObject(l)
            parse_data[mem.name] = mem
    return parse_data

def print_diff(src, des):
    pass

def main(diff1, diff2):
    comp1 = parse_maps(diff1)
    comp2 = parse_maps(diff2)

    added_dict = { k:v for k,v in comp1.items() if k not in comp2 }
    removed_dict = { k:v for k,v in comp2.items() if k not in comp1 }
    increased_dict = {}
    decreased_dict = {}

    existed_obj = [ obj for obj in comp1.values() if obj.name in comp2 ]
    for obj in existed_obj:
        key = obj.name
        diff_obj = comp2[key]
        if obj.sum > diff_obj.sum:
            increased_dict[key] = [ obj, diff_obj ]
        elif obj.sum < diff_obj.sum:
            decreased_dict[key] = [ obj, diff_obj ]

if __name__ == '__main__':
    if len(sys.argv) > 2:
        diff1 = sys.argv[1]
        diff2 = sys.argv[2]
    else:
        print("Usage : python diffsmaps.py file1 file2")
        exit(-1)

    if os.path.isfile(diff1) == False or os.path.isfile(diff2) == False:
        print("Please check file");
        exit(-1)

    main(diff1, diff2)
