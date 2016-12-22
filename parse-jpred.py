#!/usr/bin/env python
import sys
import argparse
import itertools

def parse_jpred(json, fasta):
    print 'test'
    sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs jpred data in tabular format')
    parser.add_argument('json', type=argparse.FileType("r"), help='jpred json file')
    parser.add_argument('fasta', type=argparse.FileType("r"), help='fasta file for protein')
    args = parser.parse_args()
    parse_jpred(**vars(args))
