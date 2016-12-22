#!/usr/bin/env python
import sys
import argparse
import itertools

def parse_jpred(name, jalview):
    for line in jalview:
        l = line.split('\t')
        try:
            if l[1] == 'jnetpred':
                data = l[len(l)-1].strip()
                H = data.count('H')
                E = data.count('E')
                length = len(data.split('|'))
                d = [name[:-8], name[-7:][:-4], str(length), str(H), str(E), str(float(H)/float(length)*100), str(float(E)/float(length)*100)]
                print '\t'.join(d)
        except:
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs jpred data in tabular format')
    parser.add_argument('name', type=str, help='.name file')
    parser.add_argument('jalview', type=argparse.FileType("r"), help='.jalview file')
    args = parser.parse_args()
    parse_jpred(**vars(args))
