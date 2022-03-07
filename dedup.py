#!/usr/bin/env python3

from sys import stdin,stderr,stdout
from re import compile,match,sub,split
from hashlib import md5
from collections import Counter
from json import loads

if __name__ == '__main__':
    ratio = 0.1

    counts = Counter()
    docs = []
    used = set()

    for line in stdin:
        j = loads(line)
        i,h = list(j.items())[0]

        docs += [ [i, h, 0] ]
        counts.update(h)

    # update counts
    for doc in docs:
        doc[2] = sum([ counts[h] > 1 for h in doc[1] ])

    for doc in sorted(docs, key=lambda doc: doc[2]/len(doc[1])):
        r = doc[2]/len(doc[1])

        if r <= ratio:
            print(doc[0], r)
            used.update(doc[1])
        else:
            # recalculate ratio against only already written hashes
            ra = sum([ x in used for x in doc[1] ])/len(doc[1])
            
            if ra <= ratio:
                print(doc[0], r, ra, '# after')
                used.update(doc[1])
            else:
                print('skipped', doc[0], r, ra, '# after')


print(len(used), len(counts), sum([ x for x in counts.values() ]))
