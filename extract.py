#!/usr/bin/env python3

from sys import argv,stdin,stderr,exit
from utils import chunker
from tqdm import tqdm

if __name__ == '__main__':
    if len(argv) != 2:
        print(f'usage: {argv[0]} <dedup-file>', file=stderr)
        exit(1)

    urls = set()
    with open(argv[1]) as f:
        for line in tqdm(f):
            line = ' '.join(line.split()[0:2])
            urls.add(line)
            #print(line)

    for i,chunk in chunker(stdin):
        if i in urls:
            print('## START ## ' + i)
            print(chunk)
        else:
            print(f'skipped {i}', file=stderr)

