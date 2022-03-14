#!/usr/bin/env python3

from sys import argv,stdin,stderr,exit
from utils import chunker
from tqdm import tqdm
from collections import Counter
from re import split
from math import log2

if __name__ == '__main__':
    c = Counter()

    for i,chunk in chunker(stdin):
        words = split(r'[:,.!? \n]+', chunk)
        c.update([ 2**int(log2(len(words))) ])

    for k in sorted(c):
        print(k,c[k])
