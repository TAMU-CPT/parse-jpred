#!/usr/bin/env python
import sys
import argparse
import itertools

def parse_jpred(name, jalview):
    print name
    for line in jalview:
        l = line.split('\t')
        try:
            if l[1] == 'jnetpred':
                print l[len(l)-1]
        except:
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs jpred data in tabular format')
    parser.add_argument('name', type=str, help='.name file')
    parser.add_argument('jalview', type=argparse.FileType("r"), help='.jalview file')
    args = parser.parse_args()
    parse_jpred(**vars(args))
