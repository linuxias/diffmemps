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
        return int(self._sum)

    @property
    def s_code(self):
        return int(self._s_code)

    @property
    def s_data(self):
        return int(self._s_data)

    @property
    def p_code(self):
        return int(self._p_code)

    @property
    def p_data(self):
        return int(self._p_data)

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

    added_dict = { k:v for k,v in comp2.items() if k not in comp1 }
    removed_dict = { k:v for k,v in comp1.items() if k not in comp2 }
    increased_dict = {}
    decreased_dict = {}

    existed_obj = [ obj for obj in comp1.values() if obj.name in comp2 ]
    for obj in existed_obj:
        key = obj.name
        diff_obj = comp2[key]
        if obj.sum < diff_obj.sum:
            increased_dict[key] = [ obj, diff_obj ]
        elif obj.sum > diff_obj.sum:
            decreased_dict[key] = [ obj, diff_obj ]

    with open('./result.csv', 'w', newline='') as csvf:
        def write_diff_dict(data):
            fieldnames = ['OBJECT NAME', 'SUM',
                'S(CODE)1', 'S(CODE)2', 'S(CODE) DIFF',
                'S(DATA)1', 'S(DATA)2', 'S(DATA) DIFF',
                'P(CODE)1', 'P(CODE)2', 'P(CODE) DIFF',
                'P(DATA)1', 'P(DATA)2', 'P(DATA) DIFF' ]
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)
            writer.writeheader()
            for v in data.values():
                src, diff = v
                writer.writerow({
                    'OBJECT NAME':src.name, 'SUM' : str(diff.sum-src.sum),
                    'S(CODE)1' : src.s_code,'S(CODE)2' : diff.s_code,'S(CODE) DIFF' : str(src.s_code-diff.s_code),
                    'S(DATA)1' : src.s_data,'S(DATA)2' : diff.s_data,'S(DATA) DIFF' : str(src.s_data-diff.s_data),
                    'P(CODE)1' : src.p_code,'P(CODE)2' : diff.p_code,'P(CODE) DIFF' : str(src.p_code-diff.p_code),
                    'P(DATA)1' : src.p_data,'P(DATA)2' : diff.p_data,'P(DATA) DIFF' : str(src.p_data-diff.p_data)})

        def write_dict(data):
            fieldnames = ['OBJECT NAME', 'SUM',
                'S(CODE)', 'S(DATA)', 'P(CODE)', 'P(DATA)' ]
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)
            writer.writeheader()
            for v in data.values():
                writer.writerow({
                    'OBJECT NAME':v.name, 'SUM' : v.sum,
                    'S(CODE)' : v.s_code, 'S(DATA)' : v.s_data,
                    'P(CODE)' : v.p_code, 'P(DATA)' : v.p_data})

        csvf.write('Increased memory\n')
        write_diff_dict(increased_dict)
        csvf.write('\nDecreased memory\n')
        write_diff_dict(decreased_dict)
        csvf.write('\nAdditional component\n')
        write_dict(added_dict)
        csvf.write('\nRemoved component\n')
        write_dict(removed_dict)


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
